import json
import csv

with open('Zoning_RCO-6p.geojson') as rco_file:
  file_contents = rco_file.read()

def open_csv():
    with open('data-updates.csv') as csv_file:
        csv_read=csv.reader(csv_file, delimiter=',')
        return list(csv_read)

parsed_json = json.loads(file_contents)

csv_data = open_csv()

def get_csv_by_objectid(i):
  for row in csv_data:
    if (row[0] == i):
        return row

rows = []

for i,row in enumerate(parsed_json['features']):
    id = str(row['properties']['OBJECTID'])
    csv_row = get_csv_by_objectid(id)
    parsed_json['features'][i]['properties']['ORG_TYPE_LABEL'] = csv_row[3]
    parsed_json['features'][i]['properties']['ORGANIZATION_WEBSITE'] = csv_row[4]

with open('data.geojson', 'w', encoding='utf-8') as f:
    json.dump(parsed_json, f, ensure_ascii=False)