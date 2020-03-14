#!/usr/bin/env bash

rm -rf geojson
mkdir geojson

yarn

yarn shp2json shp/countries/ne_50m_admin_0_countries.shp -o geojson/countries.geojson
yarn shp2json shp/mapunits/ne_50m_admin_0_map_units.shp -o geojson/mapunits.geojson
