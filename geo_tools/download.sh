#!/usr/bin/env bash
set -e

rm -rf *.zip shp
mkdir shp

wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_countries.zip -O countries.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_map_units.zip -O units.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_map_subunits.zip -O subunits.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_1_states_provinces_lakes.zip -O states.zip

unzip countries.zip -d shp/countries
unzip units.zip -d shp/units
unzip subunits.zip -d shp/subunits
unzip states.zip -d shp/states

rm *.zip
