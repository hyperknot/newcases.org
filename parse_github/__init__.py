import csv
import io

import requests

TIME_SERIES_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'


def get_github_csv():
    r = requests.get(TIME_SERIES_URL)
    r.raise_for_status()

    return r.text


def parse_csv(text):
    records = csv.DictReader(io.StringIO(text))
    return records
