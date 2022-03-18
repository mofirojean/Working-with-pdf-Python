import PyPDF2


"""getting and reading a pdf document"""
# open the pdf in read binary mode storing it in a variable
pdf_file_odj = open("meetingminutes.pdf", "rb")
# we get a pdf object that represents this pdf and stores it in a reader
pdf_reader = PyPDF2.PdfFileReader(pdf_file_odj)
# to get the number of pages
pdf_reader.numPages

# we use the page object to represent the single page
page_obj = pdf_reader.getPage(0)
t = page_obj.extractText()
# print(t)

"""decrypting a pdf document"""
pdf_reader2 = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))
# checking if a file is encrypted
pdf_reader2.isEncrypted
pdf_reader2.decrypt('rosebud')
page_obj2 = pdf_reader2.getPage(0)

"""creating PDFs"""
# you can't write directly to pdf file using this module
# instead it simply allows you to copy text from one pdf file and paste it another pdf file
"""
procedure:
first open multiple file
second create a pdf_file_object
third copy objects from the pdf_reader_objects to the pdf_file_writer
fourth use the PdfFileWriter object to write the output pdf"""

# opening the various pdfs in read binary mode
pdf1_file = open('meetingminutes.pdf', 'rb')
pdf2_file = open('meetingminutes2.pdf', 'rb')
# reading them
pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)
pdf2_reader = PyPDF2.PdfFileReader(pdf2_file)

#the pdf_writer represents a blank pdf document
pdf_writer = PyPDF2.PdfFileWriter()

"""this copies all the pages from the two documents and adds it to the PdfFileWriter"""
for pageNum in range(pdf1_reader.numPages):
    pageObj = pdf1_reader.getPage(pageNum)
    pdf_writer.addPage(pageObj)

for pageNum in range(pdf2_reader.numPages):
    pageObj = pdf2_reader.getPage(pageNum)
    pdf_writer.addPage(pageObj)

# here we write the copied pages from the two into one pdf document
pdfOutputFile = open('combinedminutes.pdf', 'wb')
# the write method passes the file into the write object
pdf_writer.write(pdfOutputFile)
pdfOutputFile.close()
pdf1_file.close()
pdf2_file.close()