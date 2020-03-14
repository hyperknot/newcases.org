#!/usr/bin/env bash

deactivate
rm -rf venv
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pip install -e parse_github

