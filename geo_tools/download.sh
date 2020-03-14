#!/usr/bin/env bash
set -e

rm -rf *.zip shp
mkdir shp

wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_countries.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_map_units.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_map_subunits.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_1_states_provinces_lakes.zip

unzip ne_50m_admin_0_countries.zip -d shp/countries
unzip ne_50m_admin_0_map_units.zip -d shp/units
unzip ne_50m_admin_0_map_subunits.zip -d shp/subunits
unzip ne_50m_admin_1_states_provinces_lakes.zip -d shp/states

rm *.zip
