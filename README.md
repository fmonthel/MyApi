# MyAPI

Flox-arts.net API

On MACOS :

    cp rest_api/settings.py.tpl rest_api/settings.py
    sudo pip install -r requirements.txt --upgrade
    export PYTHONPATH=.:$PYTHONPATH
    python rest_api/app.py


On Linux :

    cp rest_api/settings.py.tpl rest_api/settings.py
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt --upgrade
    export PYTHONPATH=.:$PYTHONPATH
    python3 rest_api/app.py

This repository contains boilerplate code for a RESTful API based on Flask and Flask-RESTPlus.

The code of this demo app is described in an article on my blog:
http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
