import requests

from newcases_lib import config


def download_url(url: str, filename: str):
    r = requests.get(url)
    r.raise_for_status()

    file_path = config.download_cache / filename

    with open(file_path) as outfile:
        outfile.write(r.content)
