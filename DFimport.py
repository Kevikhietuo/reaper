import glob

def dfImport(pathName):
    pdfFiles = glob.glob(pathName + '/*.pdf')
    for f in pdfFiles:
        print (f);