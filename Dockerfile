FROM python:3-onbuild

EXPOSE 8080
ENTRYPOINT uwsgi -i /usr/src/app/uwsgi_config.ini