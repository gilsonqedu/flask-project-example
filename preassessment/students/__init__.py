# -*- coding: utf-8 -*-

from flask import Blueprint

students = Blueprint('students', __name__)

from . import routes
