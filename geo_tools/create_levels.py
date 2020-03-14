#!/usr/bin/env python3
import pathlib

from newcases_lib.config import geo_tools_dir
from newcases_lib.utils import read_json, write_json

countries = read_json(geo_tools_dir / 'geojson' / 'countries.geojson')['features']
print(f'{len(countries)} countries')

units = read_json(geo_tools_dir / 'geojson' / 'units.geojson')['features']
print(f'{len(units)} units')

subunits = read_json(geo_tools_dir / 'geojson' / 'subunits.geojson')['features']
print(f'{len(subunits)} subunits')

states = read_json(geo_tools_dir / 'geojson' / 'states.geojson')['features']
print(f'{len(states)} states')

levels = dict()
iso_seen = set()

for feature in subunits:
    prop = feature['properties']
    for key in prop:
        prop[key.lower()] = prop.pop(key)

    country_name = prop['admin']
    country_iso = prop['adm0_a3']

    unit_name = prop['geounit']
    unit_iso = prop['gu_a3']

    subunit_name = prop['subunit']
    subunit_iso = prop['su_a3']

    pop = prop['pop_est']
    if pop < 1000:
        continue

    levels.setdefault(country_name, {'iso0': country_iso, 'sub1': {}})

    sub1 = levels[country_name]['sub1']
    sub1.setdefault(unit_name, {'iso1': unit_iso, 'src': 'unit', 'sub2': {}})

    sub2 = sub1[unit_name]['sub2']
    sub2.setdefault(subunit_name, {'iso2': subunit_iso, 'src': 'subunit'})

# clean up sub2
for country, country_data in levels.items():
    for data1 in country_data['sub1'].values():
        if len(data1['sub2']) == 1:
            del data1['sub2']

# clean up sub1
for country, country_data in levels.items():
    sub1 = country_data['sub1']

    if len(sub1) != 1:
        continue

    # we know there is only one element in the dict now
    sub1_first = list(sub1.values())[0]
    if 'sub2' not in sub1_first:
        del country_data['sub1']


# substitute USA, Canada sub1 regions from states file
levels['United States of America']['sub1'] = {}
levels['Canada']['sub1'] = {}
levels['Australia']['sub1'] = {}

# TODO Gibraltar missing from 50m

for feature in states:
    prop = feature['properties']
    for key in prop:
        prop[key.lower()] = prop.pop(key)

    country_name = prop['admin']
    country_iso = prop['adm0_a3']

    state_name = prop['name']
    state_iso = prop['iso_3166_2']

    if country_iso == 'USA':
        levels['United States of America']['sub1'][state_name] = {
            'iso1': state_iso,
            'src': 'states',
        }
    elif country_iso == 'CAN':
        levels['Canada']['sub1'][state_name] = {
            'iso1': state_iso,
            'src': 'states',
        }
    elif country_iso == 'AUS':
        levels['Australia']['sub1'][state_name] = {
            'iso1': state_iso,
            'src': 'states',
        }

write_json(pathlib.Path('levels.json'), levels, indent=2)
