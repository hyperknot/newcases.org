#!/usr/bin/env python3

from newcases_lib.config import export_dir
from newcases_lib.country_levels import get_geojson
from newcases_lib.jhu import get_timeseries
from newcases_lib.utils import write_json

timeseries_data = get_timeseries()

featurecollection = {'type': 'FeatureCollection', 'features': []}

for clid, data in timeseries_data.items():
    geojson = get_geojson(clid)
    featurecollection['features'].append(geojson)


export_dir.mkdir(parents=True, exist_ok=True)
write_json(export_dir / 'world.geojson', featurecollection)
write_json(export_dir / 'timeseries.json', timeseries_data, separators=(',', ':'))
