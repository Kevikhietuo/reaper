import glob
from PyPDF2 import PdfFileReader

def metadataImport(pathName):
    pdfFiles = glob.glob(pathName + '/*.pdf')
    dir = pdfFiles[0]

    with open(dir, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title

    print("AUTHOR: \t", author)
    print("CREATED ON: \t", creator)
    print("PRODUCER: \t", producer)
    print("SUBJECT: \t", subject)
    print("TITLE: \t", title)
