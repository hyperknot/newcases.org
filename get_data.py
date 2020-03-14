#!/usr/bin/env python3

import parse_github

# csv_text = parse_github.get_github_csv()
#
#
# with open('tmp.csv', 'w') as outfile:
#     outfile.write(csv_text)

with open('tmp.csv') as infile:
    csv_text = infile.read()

csv_data = parse_github.parse_csv(csv_text)
