import os

os.system('python manage.py celerycam --frequency=10.0')
os.system('python manage.py celery worker -B --concurrency=1')
