#!/usr/bin/env python3

from newcases_lib.config import geo_tools_dir
from newcases_lib.utils import read_json

countries = read_json(geo_tools_dir / 'geojson' / 'countries.geojson')['features']
print(f'{len(countries)} countries')

map_units = read_json(geo_tools_dir / 'geojson' / 'map_units.geojson')['features']
print(f'{len(map_units)} map_units')

map_subunits = read_json(geo_tools_dir / 'geojson' / 'map_subunits.geojson')['features']
print(f'{len(map_subunits)} map_subunits')

seen = set()

for feature in map_subunits:
    prop = feature['properties']

    country_name = prop['ADMIN']
    country_iso = prop['ADM0_A3']

    unit_name = prop['GEOUNIT']
    unit_iso = prop['GU_A3']

    subunit_name = prop['SUBUNIT']
    subunit_iso = prop['SU_A3']
