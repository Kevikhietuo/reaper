import csv
from csv import DictWriter
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

    df = pd.DataFrame({ 'author': [info.author],
                        'creator':[info.creator],
                        'producer':[info.producer],
                        'subject':[info.subject],
                        'title':[info.title]})
    df.to_csv(filename, index=False)