#!/usr/bin/env python

"""Distutils Setup Script."""

from setuptools import setup, find_packages

setup(name='tsw-stats',
      version='1.0',
      description='A web app to browse combat stats from "The Secret World"',
      author='David Bliss',
      license='Apache-2.0',
      url='https://github.com/proegssilb/tsw-stats',
      packages=find_packages(),
      py_modules=['main'],
      install_requires=['bottle', 'sqlalchemy', 'bottle-sqlalchemy',
                        'psycopg2', 'argh', 'alembic']
      )
