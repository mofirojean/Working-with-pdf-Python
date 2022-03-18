import PyPDF2


"""this file will rotate a pdf file"""
# open a file in read binary and then rotate a page
minutesFile = open("meetingminutes.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)

"""writing back another file"""
# copies the rotated page into our result file
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open("rotatePage.pdf", 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

