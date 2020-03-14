#!/usr/bin/env python3

import parse_github

csv_text = parse_github.get_github_csv()
csv_data = parse_github.parse_csv(csv_text)
