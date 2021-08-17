python manage.py migrate village_api
python manage.py migrate village_api

python manage.py loaddata 0001_locations
python manage.py loaddata 0002_persons
python manage.py loaddata 0003_relationships

python manage.py runserver 8000 