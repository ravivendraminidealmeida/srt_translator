#!/usr/bin/env bash
python3 -m flask db init
python3 -m flask db migrate
python3 -m flask db upgrade
python3 -m flask --app=server/src/app run --host=0.0.0.0 --port=80