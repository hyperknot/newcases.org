import csv
import datetime
import io

import requests

TIME_SERIES_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'


def get_github_csv():
    r = requests.get(TIME_SERIES_URL)
    r.raise_for_status()

    return r.text


def parse_csv(text):
    reader = csv.DictReader(io.StringIO(text), restkey='x_restkey', restval='x_restval')

    for record in reader:
        # check for too many keys
        if 'x_restkey' in record:
            raise ValueError(f'Too many items in line {reader.line_num}')

        # check for too few keys:
        if 'x_restval' in record.values():
            raise ValueError(f'Too few items in line {reader.line_num}')

    if reader.fieldnames[:4] != ['Province/State', 'Country/Region', 'Lat', 'Long']:
        raise ValueError('Wrong field names')

    date_map = create_date_map(reader.fieldnames[4:])
    print(date_map)


def create_date_map(fieldnames):
    date_map = {}

    for fieldname in fieldnames:
        dt = datetime.datetime.strptime(fieldname, '%m/%d/%y')
        iso_date = dt.date().isoformat()
        date_map[fieldname] = iso_date

    return date_map
