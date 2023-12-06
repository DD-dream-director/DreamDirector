pip install -r requirements.txt
python regenerateSecretKey.py
python manage.py migrate
python manage.py loaddata sample.json
python manage.py runserver
