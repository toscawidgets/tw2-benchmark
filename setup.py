from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tw2-benchmark',
      version=version,
      description="benchmarking tw1 vs tw2",
      long_description="",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ralph Bean',
      author_email='ralph.bean@gmail.com',
      url='threebean.wordpress.com',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "ToscaWidgets",
          "tw2.core",
          "mako",
          "genshi",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
