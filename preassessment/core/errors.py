# -*- coding: utf-8 -*-

from flask import request, jsonify

from . import core
from .exceptions import ReportsException


@core.app_errorhandler(ReportsException)
def not_found(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code

    return response
