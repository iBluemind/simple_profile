# -*- coding: utf-8 -*-

from flask import render_template
from simple_profile import app
from simple_profile.models import Photo


@app.route('/', methods=['GET'])
def index():
    stored_photos = Photo.query.all()
    return render_template('index.html', photos=stored_photos)
