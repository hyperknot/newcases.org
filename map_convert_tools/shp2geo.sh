#!/usr/bin/env bash

rm -rf geojson
mkdir geojson

yarn

yarn shp2json shp/countries/ne_50m_admin_0_countries.shp -o geojson/countries.geojson
yarn shp2json shp/map_units/ne_50m_admin_0_map_units.shp -o geojson/map_units.geojson
yarn shp2json shp/map_subunits/ne_50m_admin_0_map_subunits.shp -o geojson/map_subunits.geojson
