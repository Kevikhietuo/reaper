import csv
from csv import writer
import os
import pandas as pd

def insert_data(info):
    filename = 'reaper.csv'
    if not (os.path.isfile(filename)): #file does not exists
        headers = ['author', 'creator', 'producer', 'subject', 'title']

        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(headers)
            csvfile.close()
    
    row = [info.author, info.creator, info.producer, info.subject, info.title]
    
    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(row)

    """
    df = pd.DataFrame({ 'author': [info.author],
                        'creator':[info.creator],
                        'producer':[info.producer],
                        'subject':[info.subject],
                        'title':[info.title]})
    df.to_csv(filename, index=False)
    """