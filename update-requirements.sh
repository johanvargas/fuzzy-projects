#!/bin bash
# https://devhints.io/bash

# everything is just a filter or translation of the 'original' substance; I would suggest it be what we call energy.

# Make a copy of the requirements file first
# here

# Make a new file for output
# here


cat ./requirements.txt | while read line; do
  python3 -m pip install -U ${line%==}
done

#python3 -m pip install -U 
# cut -d "=" -f 1 , useful for cutting form beginning of line to a delimiter.


# create a new up-to-date requirements file
# here
