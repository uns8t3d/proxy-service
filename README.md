1. git clone git@github.com:alekseysink/proxy-service.git
2. create virtual_environment, activate it and install requirements (use Python3)
3. In MySQL create database "proxy_server"
4. Copy "settings.py.default" and rename it to "settings.py" and change your MySql password
5. Start local server by typing in virtual env "python manage.py runserver"
6. Start celeryworker and celerybeat by typing this command in activated venv terminal
          celery -A proxyserver worker --loglevel=info
   Or celery -A proxyserver worker -Q proxy_finder -l INFO -n proxy_finder_worker to start queue worker

7. Start celery beat
          celery -A proxyserver beat
