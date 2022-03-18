import PyPDF2


"""this program allows us to overlay information
on our pdf document."""
# useful in adding contents like adding logo, timestamps and watermarks on a page

# reading the pdf document and getting the first page
minuteFile = open("meetingminutes.pdf", 'rb')
# the getPage() method gets the first page and stores it in minutesFirstPage
pdfReader = PyPDF2.PdfFileReader(minuteFile)
minutesFirstPage = pdfReader.getPage(0)
# next we read the watermark and call mergePage() and we pass in the first page of the watermark document
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
# we add the watermark first page
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

# the loop adds the watermark to the other pages
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# we open a new pdf file and write the content inside
resultPdfFile = open("watermarkedCover.pdf", 'wb')
pdfWriter.write(resultPdfFile)
minuteFile.close()
resultPdfFile.close()
