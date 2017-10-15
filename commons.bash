#/bin/bash
# logger.bash
# by James Fulford
# creates a hard link in the provided directory


if [[ $# -lt 1 ]]; then
    echo "Please provide at least 1 command line argument"
    exit 1
fi
ln "/Users/jamesfulford/Documents/Math Capstone/commons.py" $@