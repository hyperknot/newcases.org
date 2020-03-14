#!/usr/bin/env python3

from newcases_lib.config import geo_tools_dir
from newcases_lib.utils import read_json

countries = read_json(geo_tools_dir / 'geojson' / 'countries.geojson')['features']
print(f'{len(countries)} countries')

units = read_json(geo_tools_dir / 'geojson' / 'units.geojson')['features']
print(f'{len(units)} units')

subunits = read_json(geo_tools_dir / 'geojson' / 'subunits.geojson')['features']
print(f'{len(subunits)} subunits')

states = read_json(geo_tools_dir / 'geojson' / 'states.geojson')['features']
print(f'{len(states)} states')

seen = set()

for feature in states + subunits:
    prop = feature['properties']

    for key in prop:
        prop[key.lower()] = prop.pop(key)

    country_name = prop['admin']
    country_iso = prop['adm0_a3']

    if 'subunit' in prop:
        unit_name = prop['geounit']
        unit_iso = prop['gu_a3']

        subunit_name = prop['subunit']
        subunit_iso = prop['su_a3']

    elif 'iso_3166_2' in prop:
        state_name = prop['name']
        state_iso = prop['iso_3166_2']

    else:
        print(f'Wrong feature: {prop}')
