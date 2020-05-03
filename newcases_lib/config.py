import pathlib

from newcases_lib.utils import read_json

lib_dir = pathlib.Path(__file__).parent.resolve()

root_dir = lib_dir.parent
country_levels_dir = root_dir / 'node_modules' / 'country-levels'

iso1_codes = read_json(country_levels_dir / 'iso1.json')
