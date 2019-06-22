import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='k2_cli',
    version='0.0.2',
    author_email='simon.emmott@yahoo.co.uk',
    author='Simon Emmott',
    description='A command line interface for K2 application environments',
    packages=['k2_cli', 'tests'],
    long_description=read('README.md'),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        k2=k2_cli.cli:k2
    ''',
)