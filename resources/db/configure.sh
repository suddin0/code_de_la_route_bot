#!/bin/sh

## This is a generated script in goal of configuring medias and databases related all domaines
## For more information please visit https://github.com/suddin0/codeDeLaRouteBot

## Saves the current directory path
BASE_MOD_PATH=$(pwd)

## Execute all scripts to download medias
cd ./envoituresimone.com/series/1
sh ./downloadMedia.sh
cd $BASE_MOD_PATH
cd ./envoituresimone.com/series/2
sh ./downloadMedia.sh
cd $BASE_MOD_PATH


## Create Database for all domains and series
sqlite3 data.db < globalData.SQL
