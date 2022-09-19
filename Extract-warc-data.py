from fastwarc.warc import ArchiveIterator
from fastwarc.stream_io import *
import csv

stream = GZipStream(FileStream('Lic_by_Lang_no_NoBoilerplate_true_MinHtml_true-r-00018.seg-00000.warc.gz', 'rb'))
content = []
dates = []
headers = []
urls = []

for record in ArchiveIterator(stream, parse_http=False):
    date = record.record_date
    header = record.headers
    body = record.reader.read()
    content.append(body)
    dates.append(date)
    headers.append(header)

for header in headers:
    urls.append(header['WARC-Target-URI'])

decoded_content = []

for item in content:
    decoded = item.decode('utf-8')
    decoded_content.append(decoded)

with open("output.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='\n')
    for i in range(len(dates)):
        data = [dates[i], urls[i], decoded_content[i]]
        writer.writerow(data)