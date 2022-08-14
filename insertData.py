import os
import pandas as pd

def insert_data(info):
    filename = 'reaper.xlsx'
    if (os.path.isfile(filename)): #file already exists
        df = pd.DataFrame({ 'author':info.author,
                            'creator':info.creator,
                            'producer':info.producer,
                            'subject': info.subject,
                            'title':info.title})
        df.to_excel(filename, sheet_name='reapers', index=False)
        
    else: #file does not exist
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        writer.save()
        df = pd.read_excel(filename)
        df.columns = ['author', 'creator', 'producer', 'subject', 'title']