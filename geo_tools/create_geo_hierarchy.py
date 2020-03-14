#!/usr/bin/env python3

from newcases_lib import config
from utils import read_json

countries_geojson = read_json(config.geo_tools_dir / 'geojson' / 'countries.geojson')

print(countries_geojson)
