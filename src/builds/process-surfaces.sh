#!/bin/bash

#!/bin/bash

FILTERDIR=$1

# Filter Las
find $FILTERDIR -name "*.laz" | xargs -P 10 -t -I % make surfaces pc=%