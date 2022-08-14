import xlsxwriter
import os
import pandas as pd

def insert_data(info):
    filename = 'reaper.xlsx'
    if (os.path.isfile(filename)): #file already exists
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        worksheet.write('author', info.author)
        worksheet.write('creator', info.creator)
        worksheet.write('producer', info.producer)
        worksheet.write('subject', info.subject)
        worksheet.write('title', info.title)

        workbook.close()

        # df = pd.DataFrame({ 'author': [info.author],
        #                     'creator':[info.creator],
        #                     'producer':[info.producer],
        #                     'subject':[info.subject],
        #                     'title':[info.title]})
        # df.to_excel(filename, sheet_name='reapers', index=False)
        
    else: #file does not exist
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        writer.save()
        df = pd.read_excel(filename)
        df.columns = ['author', 'creator', 'producer', 'subject', 'title']