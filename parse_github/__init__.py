import csv
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
            raise ValueError(f'too many items in line {reader.line_num}')

        # check for too few keys:
        if 'x_restval' in record.values():
            raise ValueError(f'too few items in line {reader.line_num}')
