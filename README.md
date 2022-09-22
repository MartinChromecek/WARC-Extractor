# WARC/ARC file processing

Repository that holds Python script to extract metadata and content from web archive files (WARC, ARC) and saves the output into `csv` files.

## Installation
`pip install -r requirements.txt` will install all dependencies for this project.

## Setup
Files should be stored as WARC or ARC files either uncompressed or compressed in *.gz format `WARC files` folder.
The main script `Extract-warc-data.py` will process every valid file in the `WARC files` folder. The output csv files will be exported to the ouput folder.
