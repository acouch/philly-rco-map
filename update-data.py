import json
import csv
import re

with open('Zoning_RCO-6p.geojson') as rco_file:
  file_contents = rco_file.read()

def open_csv():
    with open('data-updates.csv') as csv_file:
        csv_read=csv.reader(csv_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        return list(csv_read)

parsed_json = json.loads(file_contents)

csv_data = open_csv()

def get_csv_row_by_name(name):
  for row in csv_data:
    if (row[1] == name):
        return row

rows = []

for i,row in enumerate(parsed_json['features']):
    name = str(row['properties']['organization_name'])
    csv_row = get_csv_row_by_name(name)
    if not csv_row:
       print(f"Can't find {name}, id {parsed_json['features'][i]['properties']['lni_id']}")
    else:
      lni_id = csv_row[0]
        
      parsed_json['features'][i]['properties']['ORG_TYPE_LABEL'] = csv_row[2]
      parsed_json['features'][i]['properties']['ORG_MISSION'] = csv_row[4]
      if (csv_row[5]):
          parsed_json['features'][i]['properties']['ORG_LOGO'] = lni_id + '.' + csv_row[5]

with open('data.geojson', 'w', encoding='utf-8') as f:
    json.dump(parsed_json, f, ensure_ascii=False)

index = {} 
for rco in parsed_json['features']:
  lni_id = int(rco['properties']['lni_id']) 
  index[lni_id] = rco['properties']['organization_name']
  with open(f"rcos/{lni_id}.geojson", 'w', encoding='utf-8') as f:
    json.dump(rco, f, ensure_ascii=False)

with open('rcos/index.json', 'w', encoding='utf-8') as f:
  json.dump(index, f, ensure_ascii=False)
