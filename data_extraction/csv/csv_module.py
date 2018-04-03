import csv
import datetime
from pathlib import Path
from pprint import pprint

data_path = Path('waypoints.csv')


def clean_row(source_row):
    source_row['lat_n']= float(source_row['lat'])
    source_row['lon_n']= float(source_row['lon'])
    source_row['ts_date']= datetime.datetime.strptime(source_row['date'],'%Y-%m-%d').date()
    source_row['ts_time']= datetime.datetime.strptime(source_row['time'],'%H:%M:%S').time()
    source_row['timestamp']= datetime.datetime.combine(
        source_row['ts_date'],
        source_row['ts_time'])
    return source_row

def cleanse(reader):
    for row in reader:
        yield clean_row(row)

with data_path.open('r') as data_file:
    data_reader = csv.DictReader(data_file)
    for data in cleanse(data_reader):
        pprint(data)


