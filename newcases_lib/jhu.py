import csv
import datetime
import io
import pathlib

import requests

from newcases_lib.country_levels import levels
from newcases_lib.utils import write_json


def get_timeseries():
    iso_lookup = get_iso_lookup()

    urls = {
        'confirmed': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        'deaths': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
        'recovered': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv',
    }

    mixed = dict()

    for kind, url in urls.items():
        data = parse_jhu_csv(url, iso_lookup)
        for countrylevel_id, case_data in data.items():
            mixed.setdefault(countrylevel_id, dict())
            for date, number in case_data.items():
                mixed[countrylevel_id].setdefault(date, dict())
                mixed[countrylevel_id][date][kind] = number

    return mixed


def get_iso_lookup():
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'

    r = requests.get(url)
    r.raise_for_status()

    reader = csv.DictReader(io.StringIO(r.text), restkey='x_restkey', restval='x_restval')

    assert reader.fieldnames == [
        'UID',
        'iso2',
        'iso3',
        'code3',
        'FIPS',
        'Admin2',
        'Province_State',
        'Country_Region',
        'Lat',
        'Long_',
        'Combined_Key',
        'Population',
    ]

    lookup = {}

    for record in reader:
        # check for too many keys
        if 'x_restkey' in record:
            raise ValueError(f'Too many items in line {reader.line_num}')

        # check for too few keys:
        if 'x_restval' in record.values():
            raise ValueError(f'Too few items in line {reader.line_num}')

        country = record['Country_Region']
        state = record['Province_State']
        key = f'{country}#{state}'

        country_code = record['iso2']

        # skip ships
        if not country_code:
            continue

        # process US later
        if country_code == 'US' or record['FIPS']:
            continue

        if state:
            continue

        iso1_data = levels['iso1'][country_code]
        lookup[key] = iso1_data['countrylevel_id']

    return lookup


def parse_jhu_csv(url, iso_lookup):
    r = requests.get(url)
    r.raise_for_status()

    reader = csv.DictReader(io.StringIO(r.text), restkey='x_restkey', restval='x_restval')

    assert reader.fieldnames[:4] == ['Province/State', 'Country/Region', 'Lat', 'Long']

    data = dict()

    for record in reader:
        # check for too many keys
        if 'x_restkey' in record:
            raise ValueError(f'Too many items in line {reader.line_num}')

        # check for too few keys:
        if 'x_restval' in record.values():
            raise ValueError(f'Too few items in line {reader.line_num}')

        country = record['Country/Region']
        state = record['Province/State']
        key = f'{country}#{state}'

        if country == 'US':
            continue

        if country in ['Diamond Princess', 'MS Zaandam']:
            continue

        if state:
            print(key)
            continue

        assert key in iso_lookup

        countrylevel_id = iso_lookup[key]

        case_data = {}
        for key, value in record.items():
            if key in ['Province/State', 'Country/Region', 'Lat', 'Long']:
                continue
            dt = datetime.datetime.strptime(key, '%m/%d/%y')
            iso_date = dt.date().isoformat()

            case_data[iso_date] = int(value)

        if countrylevel_id in data:
            print(f'already seen: {countrylevel_id}')

        data[countrylevel_id] = case_data

    return data
