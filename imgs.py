import json
import csv
import re
import requests
from PIL import Image

def open_csv():
    with open('data-updates.csv') as csv_file:
        csv_read=csv.reader(csv_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        return list(csv_read)

csv_data = open_csv()

def get_csv_by_objectid(i):
  for row in csv_data:
    if (row[0] == i):
        return row

rows = []

for i,row in enumerate(csv_data):
    if (row[6] and i > 0):
        url = row[7]
        data = requests.get(url)
        id = row[0]
        file_type = data.headers['content-type']
        ext = '';
        if (file_type == 'image/svg+xml'): 
            ext = 'svg'
        elif (file_type == 'image/jpeg'):
            ext = 'jpg'
        elif (file_type == 'image/jpg'):
            ext = 'jpg'
        elif (file_type == 'image/png'):
            ext = 'png'
        elif (file_type == 'image/gif'):
            ext = 'gif'
        if (ext == ''):
            print(url)
            print(file_type, data.status_code, id)
        else:
            path = 'imgs/logos/' + id + '.' + ext
            f = open(path,'wb')
            f.write(data.content)
            f.close()


