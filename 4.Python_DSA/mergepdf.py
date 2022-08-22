import PyPDF2
print("start to merged the file")
try:
    pdf1file = open('1.pdf', 'rb')
    pdf2file = open('2.pdf', 'rb')
    print("okkkkkkk")
    # read the file that you have open
    pdf1reader = PyPDF2.PdfFileReader(pdf1file)
    pdf2reader = PyPDF2.PdfFileReader(pdf2file)
    print("okkkkkkk")
    # create the new pdffilewriter whiich represent the new pdf
    pdfwriter = PyPDF2.PdfFileWriter()
    print("okkkkkkk")
    # loop threough all the pagenumber fo rthe first document
    for pagenum in range(pdf1reader.numPages):
        pageobj = pdf1reader.getPage(pagenum)
        pdfwriter.addPage(pageobj)
    print("okkkkkkk")
    # loop through all the page of the second doocumrnt
    for pagenum in range(pdf2reader.numPages):
        pageobj = pdf2reader.getPage(pagenum)
        pdfwriter.addPage(pageobj)
    print("okkkkkkk")

    pdfoutputfile = open("merge.pdf", 'wb')
    pdfwriter.write(pdfoutputfile)
    print("okkkkkkk")
    pdfoutputfile.close()
    pdf1file.close()
    pdf2file.close()
    print("your pdf is now merged")
except:
    print("There are some error")
