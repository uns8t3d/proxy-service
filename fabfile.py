import os
from fabric.api import cd, env, run, local, sudo

local_app_dir = './'

project_root_name = 'proxy'
project_name = "proxy-service"
remote_dir = "/opt"
remote_deploy_dir = os.path.join(remote_dir, project_root_name)
remote_app_dir = os.path.join(remote_deploy_dir, project_name)
remote_virtualenv_dir = os.path.join(remote_deploy_dir, project_root_name + "_env")

deploy_user = "root"
deploy_password = "7VJEuqQ7b5"

branch = "master"

db_name = "proxy"
db_user = "root"
db_password = "X9BlOVKbG3"
db_create_str = "\"create database {db_name};\""
db_create_str = db_create_str.format(db_name=db_name)


env.forward_agent = True
env.hosts = ['67.205.186.116']

package_list = ["python-virtualenv", "supervisor", "nginx", "mysql-server", "git", "libmysqlclient-dev", "libxml2-dev",
                "libxslt-dev", "rabbitmq-server", "python-dev"]


def prepare_remote_env():
    set_prepare_env()
    run("apt-get update")
    run("apt-get -y --no-upgrade install %s" % " ".join(package_list))
    run("mkdir %s" % remote_deploy_dir)
    run("mysql -u root -p %s" % db_create_str)
    run("/etc/init.d/mysql start")


def set_prepare_env():
    env.user = "root"
    env.password = "7VJEuqQ7b5"

    #result = local('vagrant global-status | grep running', capture=True)
    #machineId = result.split()[0]

    # use vagrant ssh key for the running VM
    #result = local('vagrant ssh-config {} | grep IdentityFile'.format(machineId), capture=True)

    #env.key_filename = result.split()[1]


def set_deploy_env():
    env.user = deploy_user
    env.password = deploy_password


def provisioning():
    set_deploy_env()
    with cd(remote_deploy_dir):
        run("virtualenv %s" % remote_virtualenv_dir)
        run("git clone -b %s git@github.com:Eyeless95/proxy-service.git" % branch)
        run("%s/bin/pip install -r %s" % (remote_virtualenv_dir, os.path.join(remote_app_dir, "requirements.txt")))
        run("%s/bin/python fba_reimbursement/manage.py migrate" % remote_virtualenv_dir)
        run("%s/bin/python fba_reimbursement/manage.py collectstatic --no-input" % remote_virtualenv_dir)

        # run("mkdir proxy-service/logs")

        sudo("cp proxy-service/config/proxy.conf /etc/supervisor/conf.d/")
        sudo("cp proxy-service/config/proxy_celery.conf /etc/supervisor/conf.d/")
        sudo("cp proxy-service/config/proxy_celerybeat.conf /etc/supervisor/conf.d/")
        sudo("cp proxy-service/config/proxy_nginx.conf /etc/nginx/sites-enabled/")
        sudo("/etc/init.d/supervisor restart")
        sudo("/etc/init.d/nginx restart")


def deploy():
    set_deploy_env()
    with cd(remote_app_dir):
        run("git fetch")
        run("git checkout %s" % branch)
        run("git pull")
        run("%s/bin/pip install -r %s" % (remote_virtualenv_dir, os.path.join(remote_app_dir, "requirements.txt")))

        run("%s/bin/python %s/manage.py migrate" % (remote_virtualenv_dir, remote_app_dir))
        run("%s/bin/python %s/manage.py collectstatic --no-input" % (remote_virtualenv_dir, remote_app_dir))

        sudo("cp proxy-service/config/proxy.conf /etc/supervisor/conf.d/")
        sudo("cp proxy-service/config/proxy_celery.conf /etc/supervisor/conf.d/")
        sudo("cp proxy-service/config/proxy_celerybeat.conf /etc/supervisor/conf.d/")
        sudo("cp proxy-service/config/proxy_nginx.conf /etc/nginx/sites-enabled/")
        sudo("supervisorctl reread")
        sudo("supervisorctl update")
        sudo("supervisorctl restart all")
        sudo("/etc/init.d/nginx restart")
