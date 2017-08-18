# -*- coding: utf-8 -*-

import json

from flask import jsonify, request

from . import students
from .models import Student, ExampleModel
from .schemas import students_schema


@students.route('/')
def index():
    return 'QEdu pre-assessment works!'


@students.route('/students', methods=['GET'])
def students_list():
    students = Student.objects()
    result = students_schema.dump(students)
    return jsonify(result.data)


@students.route('/examples', methods=['GET'])
def example_list():
    examples = ExampleModel.objects()
    return jsonify(examples)


@students.route('/examples', methods=['POST'])
def example_post():
    example = ExampleModel.from_json(json.dumps(request.json))
    example.save()

    return jsonify({"data": example}), 201
