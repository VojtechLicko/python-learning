# Not every PDF file can be readable by python
import PyPDF2

with open('Working_Business_Proposal.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)  # loads the pdf file
    # gets the number of the pages
    print(f"Number of pages is {pdf_reader.numPages}")
    page_one = pdf_reader.getPage(0)  # gets the page
    page_one_text = page_one.extract_text()  # extracts text from page
    # print(page_one_text)


with open("Working_Business_Proposal.pdf", 'rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)
    first_page = pdf_reader.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(first_page)
    pdf_output = open("Some_New_Doc.pdf", "wb")
    pdf_writer.write(pdf_output)


with open("Working_Business_Proposal.pdf", 'rb') as f:
    all_text = []
    pdf_reader = PyPDF2.PdfFileReader(f)
    for page in range(pdf_reader.numPages):
        current_page = pdf_reader.getPage(page)
        page_text = current_page.extract_text()
        all_text.append(page_text)
    print(all_text)
