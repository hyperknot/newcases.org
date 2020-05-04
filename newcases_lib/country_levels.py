from newcases_lib.config import country_levels_dir
from newcases_lib.utils import read_json

levels = {'iso1': read_json(country_levels_dir / 'iso1.json')}


def split_id(clid):
    parts = clid.split(':')
    assert len(parts) == 2

    level, code = parts
    assert level in levels

    return level, code


def get_location_data(clid):
    level, code = split_id(clid)
    return levels[level][code]


def get_geojson(clid):
    location_data = get_location_data(clid)
    geojson_path = location_data['geojson_path']

    feature = read_json(country_levels_dir / 'geojson' / geojson_path)
    feature['properties'] = {'id': clid}

    return feature
