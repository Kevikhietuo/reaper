import glob
import insertData
from PyPDF2 import PdfFileReader

def metadataImport(pathName):
    pdfFiles = glob.glob(pathName + '/*.pdf')
    
    for pdf in pdfFiles:
        print("CURRENT FILE: ", str(pdf))
        with open(pdf, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()

            insertData.insert_data(info)
        print("CURRENT FILE DONE \n\n")