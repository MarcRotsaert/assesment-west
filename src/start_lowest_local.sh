#!/usr/bin/env bash

port=8080
# (cd src; nohup ./start_django.sh ${port} &)
(nohup django_west/manage.py runserver ${port} &)
sleep 7
python -m webbrowser -t "http://localhost:${port}/algoritm" 