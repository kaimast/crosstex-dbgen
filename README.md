# Database Files for CrossTeX
This tool imports citation data from DBLP that then can be used in CrossTeX.

## Prerequisites
This repository should work on any modern system with python3 installed

On Ubuntu you can install the required packages like so:
```
apt install python3-lxml
```

## Installation
Note that the first two steps are optional. You can just install the xtx files already included in this repository.

```
# 1. Download bib files from DBLP
make dblp.xml.gz

# 2. (Re-)build crosstex files
make xtx

# 3. Install for the current user
make install
```

## Adding new content

First, add the conference/journal/workshop to the bottom of dblpparse.py. Then run `make clean && make xtx`

