import json
import csv

with open('Zoning_RCO.geojson') as rco_file:
  file_contents = rco_file.read()

with open('data-updates.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')

parsed_json = json.loads(file_contents)

rows = []

for row in parsed_json['features']:
   
   # update row
   print(row)


