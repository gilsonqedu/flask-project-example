# -*- coding: utf-8 -*-

import os

from flask_script import Manager, Shell
from preassessment import create_app

app = create_app(os.getenv('QEDU_REPORTS_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    """Prepare context to python shell (e.g: ipython, etc)"""
    return dict(app=app)


@manager.command
def test(coverage=False):
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    # TODO: Prepare coverage test
    if coverage:
        pass


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
