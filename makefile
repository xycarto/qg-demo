-include .creds

BASEIMAGE := xycarto/qg-demo
IMAGE := $(BASEIMAGE):2025-01-31

.PHONY:

RUN ?= docker run -i --rm --net=host \
	--user=$$(id -u):$$(id -g) \
	-e DISPLAY=$$DISPLAY \
	--env-file .creds \
	-e RUN= \
	-e HOME=/work \
	-v$$(pwd):/work \
	-w /work $(IMAGE)

PHONY: 


### CLEAN
clean: 
	$(RUN) python3 -m src.clean.clean-names

# make unzip zip=data/qld-government/point-clouds/ahd/Brisbane_2009_LGA_SW_499000_6960000_1K_Las.zip
unzip:
	$(RUN) python3 -m src.clean.unzip-las $(zip)

## INDEX
# make index dir=data/qld-government/las
index:
	$(RUN) python3 -m src.index-las $(dir)

### PROCESS
# make filter pc=data/qld-government/las/Brisbane_2009_LGA_SW_499000_6960000_1K_Las.laz
filter: 
	$(RUN) python3  src/filter-no-buff.py $(pc)

# make surfaces pc=data/qld-government/las/Brisbane_2009_LGA_SW_499000_6960000_1K_Las.laz
surfaces:
	$(RUN) python3  src/surfaces.py $(pc)

### COGS
# make cog dir=data/qld-government/dem
cog: 
	$(RUN) python3 src/cog.py $(dir)

### Vector Tiles


### BUILDS
# make process-zips dir=data/qld-government/point-clouds/ahd
process-zips:
	$(RUN) bash src/builds/process-zips.sh $(dir)

# make filter-las dir=data/qld-government/las
filter-las:
	$(RUN) bash src/builds/filter-las.sh $(dir)

# make process-surfaces dir=data/qld-government/filtered
process-surfaces:
	$(RUN) bash src/builds/process-surfaces.sh $(dir)

### TEST
pdalinfo:
	$(RUN) pdal info --summary data/qld-government/las/Brisbane_2009_LGA_SW_499000_6960000_1K_Las.laz
#	$(RUN) pdal --version
#	$(RUN) pdal info $(pc)


##### DOCKER MAIN
local-test: docker/Dockerfile
	docker run -it --rm --net=host --user=$$(id -u):$$(id -g) \
	-e DISPLAY=$$DISPLAY \
	--env-file .creds \
	-e RUN= -v$$(pwd):/work \
	-w /work $(IMAGE) \
	bash

docker-local: docker/Dockerfile
	docker build --tag $(BASEIMAGE) - < docker/Dockerfile && \
	docker tag $(BASEIMAGE) $(IMAGE)

docker: docker/Dockerfile
	docker build --tag $(BASEIMAGE) - < docker/Dockerfile  && \
	docker tag $(BASEIMAGE) $(IMAGE) && \
	docker push $(IMAGE) && \
	touch .push

docker-pull:
	docker pull $(IMAGE)