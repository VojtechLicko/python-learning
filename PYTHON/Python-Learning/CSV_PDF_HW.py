import csv
import re

import PyPDF2

# U have to set the encoding
data = open('find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
link = ""
y = 0
for y, data in enumerate(data_lines):
    link += data[y]
print(link)


with open('Find_the_Phone_Number.pdf', 'rb') as f:
    all_text = []
    pdf_reader = PyPDF2.PdfFileReader(f)
    for page in range(pdf_reader.numPages):
        current_page = pdf_reader.getPage(page)
        page_text = current_page.extract_text()
        all_text.append(page_text)

phone_pattern = re.compile(r"(\d{2,4})\S(\d{2,4})\S(\d{2,4})")
results = re.search(phone_pattern, str(all_text))
print(results)
