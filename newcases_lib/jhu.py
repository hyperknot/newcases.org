import csv
import io

import requests

from newcases_lib.config import iso1_codes


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

        iso1_data = iso1_codes[country_code]
        lookup[key] = iso1_data['countrylevel_id']

    return lookup
