# A file with the CSV file extension is a Comma Separated Values file.
# .csv file only contains the raw data from the spreadsheet
# pandas is really powerful as well with data generally
import csv

data = open('example.csv', encoding='utf-8')  # U have to set the encoding
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines[0])
all_emails = []
# all emails
for line in data_lines[1:15]:
    all_emails.append(line[3])
print(all_emails)
# all names
full_names = []
for line in data_lines[1:15]:
    full_names.append(" ".join(line[1:3]))

print(full_names)


# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'.
# New file
file_to_output = open('to_save_file.csv', 'w', newline='')

csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()


f = open('to_save_file.csv', 'a', newline='')
csv_writer = csv.writer(f)

csv_writer.writerow(['new', 'new', 'new'])
f.close()
