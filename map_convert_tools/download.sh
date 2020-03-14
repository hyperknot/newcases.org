#!/usr/bin/env bash

rm -rf *.zip shp
mkdir shp

wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_countries.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_map_units.zip
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_map_subunits.zip

unzip ne_50m_admin_0_countries.zip -d shp/countries
unzip ne_50m_admin_0_map_units.zip -d shp/map_units
unzip ne_50m_admin_0_map_subunits.zip -d shp/map_subunits

rm *.zip
