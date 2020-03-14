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

for feature in subunits:
    prop = feature['properties']

    for key in prop:
        prop[key.lower()] = prop.pop(key)

    country_name = prop['admin']
    country_iso = prop['adm0_a3']

    levels.setdefault(country_name, dict())

    unit_name = prop['geounit']
    unit_iso = prop['gu_a3']

    subunit_name = prop['subunit']
    subunit_iso = prop['su_a3']

    levels[country_name].setdefault(unit_name, dict())
    levels[country_name][unit_name].setdefault(subunit_name, dict())

# clean up sole units
for country, units in levels.items():
    for unit, subunits in units.items():
        if len(subunits) == 1:
            levels[country][unit] = {}

# clean up sole subunits
for country, units in levels.items():
    if len(units) == 1:
        levels[country] = {}

    # elif 'iso_3166_2' in prop:
    #     state_name = prop['name']
    #     state_iso = prop['iso_3166_2']
    #
    #     levels[country_name].setdefault(state_name, dict())
    #     levels[country_name][state_name].setdefault('-', dict())


write_json(pathlib.Path('levels.json'), levels, indent=2)
