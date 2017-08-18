# -*- coding: utf-8 -*-

from preassessment import db


class Student(db.Document):
    name = db.StringField()
    registration_number = db.StringField(db_field='registrationNumber')
    birth = db.StringField(db_field='birthDate')
    school = db.ReferenceField('School', dbref=True)

    meta = {
        'collection': 'students'
    }

    def __str__(self):
        return self.name


class Department(db.Document):
    description = db.StringField()
    city = db.StringField()
    state = db.StringField()
    type = db.StringField()
    image = db.StringField()
    status = db.StringField()

    meta = {
        'collection': 'departments'
    }

    def __str__(self):
        return self.description


class School(db.Document):
    description = db.StringField()
    know_as = db.StringField(db_field='knownAs')
    department = db.ReferenceField('Department', dbref=True)
    image = db.StringField()
    status = db.StringField()

    meta = {
        'collection': 'schools'
    }

    def __str__(self):
        return self.description


class ExampleModel(db.Document):
    name = db.StringField()

    meta = {
        'collection': 'examples'
    }

    def __str__(self):
        return self.name
