#!/usr/bin/env python3
import json

from newcases_lib import download_github

# csv_text = parse_github.get_github_csv()


# with open('tmp.csv', 'w') as outfile:
#     outfile.write(csv_text)

with open('tmp.csv') as infile:
    csv_text = infile.read()

data = download_github.parse_csv(csv_text)


with open('data/country_data.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)
