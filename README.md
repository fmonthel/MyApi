# MyAPI

Flox-arts.net API

On MACOS :

    cp rest_api/settings.py.tpl rest_api/settings.py
    export PYTHONPATH=.:$PYTHONPATH
    python rest_api/app.py


On Linux :

    source venv/bin/activate
    cp rest_api/settings.py.tpl rest_api/settings.py
    export PYTHONPATH=.:$PYTHONPATH
    python rest_api/app.py

This repository contains boilerplate code for a RESTful API based on Flask and Flask-RESTPlus.

The code of this demo app is described in an article on my blog:
http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
