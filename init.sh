#!/bin/bash

# this script should only be used when you want to recreate the database schema

rm -fr mysql_data

docker compose up -d --force-recreate