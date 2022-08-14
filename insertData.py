import csv
from csv import writer
import os
import pandas as pd

def insert_data(info, pathName):
    filename = 'reaper.csv'
    myPath = str(pathName) + "/" + filename
    print("THE PATH IS: ", myPath)
    
    if not (os.path.isfile(myPath)): #file does not exists
        headers = ['author', 'creator', 'producer', 'subject', 'title']

        with open(myPath, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(headers)
            csvfile.close()
    
    row = [info.author, info.creator, info.producer, info.subject, info.title]
    
    with open(myPath, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(row)