import pathlib

lib_dir = pathlib.Path(__file__).parent.resolve()

tmp_dir = lib_dir.parent / 'tmp'
download_cache = tmp_dir / 'download_cache'

# map_convert_dir = lib_dir.parent / 'map_convert'
