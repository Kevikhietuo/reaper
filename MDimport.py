import glob
import insertData
from PyPDF2 import PdfFileReader

def metadataImport(pathName):
    pdfFiles = glob.glob(pathName + '/*.pdf') #selecting only pdf files
    
    for pdf in pdfFiles:
        with open(pdf, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()

            insertData.insert_data(info, pathName)