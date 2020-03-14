#!/usr/bin/env bash

rm -rf geojson
mkdir geojson

yarn

yarn shp2json shp/countries/*.shp -o geojson/countries.geojson
yarn shp2json shp/units/*.shp -o geojson/units.geojson
yarn shp2json shp/subunits/*.shp -o geojson/subunits.geojson
yarn shp2json shp/states/*.shp -o geojson/states.geojson
