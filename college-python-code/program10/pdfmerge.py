from PyPDF2 import PdfReader, PdfWriter


num = int(input("enter the page you want to get from the pdfs"))

pdf1 = open("birds.pdf", "rb")
pdf2 = open("birdspic.pdf", "rb")

pdf_writer = PdfWriter()

pdf1_reader = PdfReader(pdf1)
pdf2_reader = PdfReader(pdf2)

page1 = pdf1_reader.pages[num - 1]
page2 = pdf2_reader.pages[num - 1]
pdf_writer.add_page(page1)
pdf_writer.add_page(page2)

with open("output.pdf", "wb") as output:
    pdf_writer.write(output)
