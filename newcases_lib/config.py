import pathlib

from newcases_lib.utils import read_json

lib_dir = pathlib.Path(__file__).parent.resolve()

root_dir = lib_dir.parent
country_levels_dir = root_dir / 'node_modules' / 'country-levels'

public_dir = root_dir / 'public'
export_dir = public_dir / 'export'
