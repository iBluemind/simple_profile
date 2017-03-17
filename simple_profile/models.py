# -*- coding: utf-8 -*-

import datetime
from sqlalchemy import func
from simple_profile import db


class Photo(db.Model):

    __tablename__ = 'photo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    path = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, onupdate=func.current_timestamp())

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.created_at = datetime.datetime.now()
