#!/bin/bash

va
pip install -r ./requirements.txt
py ./regenerateSecretKey.py
py manage.py migrate
py manage.py loaddata ./sample_db.json
py manage.py runserver

