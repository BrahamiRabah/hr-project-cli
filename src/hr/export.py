import json
import csv

def to_json_file(users, export_file):
    json.dump(users, export_file, indent=4)
    export_file.close()

def to_csv_file(users, export_file):
    export_file.write('name,id,home,shell\n')
    result = csv.writer(export_file)
    row = [[user['name'], user['id'], user['home'], user['shell']] for user in users]
    result.writerow(row)
    export_file.close()


