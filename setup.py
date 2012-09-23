from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='plex-power-tools',
      version=version,
      description="series of scripts to help maintain your Plex (http://plexapp.com/) media server",
      long_description="""\
series of scripts to help maintain your Plex (http://plexapp.com/) media server""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ken Pepple',
      author_email='ken.pepple@rabbityard.com',
      url='http://ken.pepple.info',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
