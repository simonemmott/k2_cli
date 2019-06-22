import os
from setuptools import setup
import k2_cli

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name=k2_cli.name,
    version=k2_cli.version,
    author_email=k2_cli.author_email,
    author=k2_cli.author,
    description=k2_cli.description,
    packages=['k2_cli', 'tests'],
    long_description=read('README.md'),
    install_requires=[
        'Click',
        'pyYaml',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        k2=k2_cli.cli:k2
    ''',
)