# -*- coding: utf-8 -*-

from preassessment import marshmallow

from marshmallow import fields


class StudentSchema(marshmallow.Schema):
    """
    Schema to prepare data structure to show
    to clients.

    Not recommended serializer all document, that
    contain private data, for example.
    """
    id = fields.Str()
    name = fields.Str()
    registrationNumber = fields.Str()
    birthName = fields.Date()


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
