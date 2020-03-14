import json
import pathlib

# def download_url(url: str, filename: str):
#     r = requests.get(url)
#     r.raise_for_status()
#
#     file_path = config.download_cache / filename
#
#     with open(file_path) as outfile:
#         outfile.write(r.content)


def read_json(file_path: pathlib.Path):
    with file_path.open() as infile:
        return json.load(infile)


def write_json(file_path: pathlib.Path, data, indent: int = None):
    with file_path.open('w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=indent, allow_nan=False, sort_keys=True)
