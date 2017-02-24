Proxy Service
=============


Setup with Docker
=================
1. Download project: $ git clone https://github.com/Eyeless95/proxy-service.git
2. Install Docker
3. Copy '.env.default' file from project root directory and name it '.env'. Here you can edit all info, like username and password for database etc.
4. From project root directory run: $ docker-compose build
5. After success build run: $ docker-compose up -d
6. After success go to File->Settings->Project: fba_reimbursement->Project Interpreter, click settings, choose Add Remote,
    type SSH Credentials:
    Host: 127.66.6.33 Port: 1022
    User name: root
    Password: root
    Python interpreter path: /root/venv/bin/python
7. Copy settings.py.docker and name it settings.py
8. Go to Tools -> Start SSH session and choose session with your remote venv
9. In remote venv: $ pip install -r requirements
10. Go to File->Settings->Project: proxy-service->Project Interpreter, click More... Edit your remote venv and name it ProxyEnv
11. Make sure that path mapping is: <Project root>→/usr/src/python-app
12. Go to File->Settings->Languages & Frameworks->Django: Enable Dhango support, choose project root and settings folder. Make sure that Manage script is manage.py
13. Apply migrations: $ python manage.py migrate
14. Create superuser: $ python manage.py createsuperuser
15. Run server: $ python manage.py runserver


Starting server:
================

1. Run server: $ python manage.py runserver
2. Run celery queues: $ celery -A proxyserver worker -Q proxy_finder -l INFO -n proxy_finder_worker
3. Run celery scheduler: $ celery -A proxyserver beat
