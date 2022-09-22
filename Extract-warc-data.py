import csv
import os
import fastwarc
from bs4 import BeautifulSoup as bs
from fastwarc.warc import ArchiveIterator
from fastwarc.stream_io import GZipStream
from fastwarc.stream_io import FileStream

path = os.path.join(os.getcwd(), "WARC files")
files = list(os.listdir(path))

def extractContent(file):
    file_path = os.path.join(path, file)
    stream = GZipStream(FileStream(file_path, 'rb'))
    content = []
    dates = []
    headers = []
    urls = []
    licence_info = []

    for record in ArchiveIterator(stream, parse_http=False):
        date = record.record_date
        header = record.headers
        body = record.reader.read()
        content.append(body)
        dates.append(date)
        headers.append(header)

    for header in headers:
        urls.append(header['WARC-Target-URI'])
        licence_info.append(header['c4_license'])

        decoded_content = []

    for item in content:
        decoded = item.decode('utf-8')
        soup = bs(decoded, "html.parser")
        cleaned = soup.get_text()
        decoded_content.append(cleaned)

    with open(file + ".csv", "w", encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file)
        for i in range(len(dates)):
            data = [dates[i], urls[i], licence_info[i], decoded_content[i]]
            writer.writerow(data)

for file in files:
    extractContent(file)