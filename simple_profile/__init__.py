# -*- coding: utf-8 -*-

from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_s3 import FlaskS3
from simple_profile.connectors.dao import DAO, DaoType
import os, click

app = Flask(__name__)
assets = Environment(app)
s3 = FlaskS3(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 7200
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_DATABASE_URI'] = DAO.DAO_TYPES[DaoType.PRODUCTION].uri

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['FLASKS3_BUCKET_NAME'] = os.environ.get('FLASKS3_BUCKET_NAME')
app.config['FLASKS3_REGION'] = 'ap-northeast-2'
app.config['AWS_ACCESS_KEY_ID'] = os.environ.get('AWS_ACCESS_KEY_ID')
app.config['AWS_SECRET_ACCESS_KEY'] = os.environ.get('AWS_SECRET_ACCESS_KEY')
app.config['FLASKS3_FORCE_MIMETYPE'] = True
app.config['FLASK_ASSETS_USE_S3'] = True
app.config['FLASKS3_GZIP'] = True
app.config['FLASKS3_USE_HTTPS'] = False

# 기본 응답 템플릿
def response_template(message, status=200, data=None):
    content = {'message': message}
    if data:
        content = {'message': message, 'data': data}
    import flask
    return flask.jsonify(content), status

from simple_profile.views import *

from flask_assets import Bundle
from simple_profile import assets
simpleprofile_css = Bundle('assets/css/simple_profile.css', filters='cssmin', output='gen/simple_profile.min.css')
assets.register('simpleprofile_css', simpleprofile_css)

@app.cli.command()
def initdb():
    click.echo('create all models')
    from simple_profile import db
    from simple_profile.models import Photo
    db.drop_all()
    db.create_all()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    for dirname, dirnames, filenames in os.walk('%s/static/assets/img' % dir_path):
        for filename in filenames:
            stored_photo = Photo(filename, 'assets/img/%s' % filename)
            db.session.add(stored_photo)
    db.session.commit()


@app.cli.command()
def build_compressed_assets():
    import logging
    log = logging.getLogger('webassets')
    log.addHandler(logging.StreamHandler())
    log.setLevel(logging.DEBUG)
    from webassets.script import CommandLineEnvironment
    from simple_profile import assets
    cmdenv = CommandLineEnvironment(assets, log)
    cmdenv.build()


@app.cli.command()
def upload_to_s3():
    from flask_s3 import create_all
    from simple_profile import app
    create_all(app, filepath_filter_regex=r'^(assets|gen|libs|resource|fonts)')
