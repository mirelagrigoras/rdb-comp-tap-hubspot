#!/usr/bin/env python

from setuptools import setup

setup(name='rdb-comp-tap-hubspot',
      version='0.0.0',
      description='Singer.io tap for extracting data from the HubSpot API that generates a schema that is Postgres compatible for each stream. ',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['rdb-comp-tap-hubspot'],
      install_requires=[
          'attrs==16.3.0',
          'singer-python==5.1.1',
          'requests==2.20.0',
          'backoff==1.3.2',
          'requests_mock==1.3.0',
          'nose'
      ],
      entry_points='''
          [console_scripts]
          rdb_comp_tap_hubspot=rdb_comp_tap_hubspot.rdb_comp_tap_hubspot:main
      ''',
      packages=['rdb_comp_tap_hubspot'],
      package_data = {
          'rdb_comp_tap_hubspot/schemas': [
              "campaigns.json",
              "companies.json",
              "contact_lists.json",
              "contacts.json",
              "deals.json",
              "email_events.json",
              "forms.json",
              "keywords.json",
              "owners.json",
              "subscription_changes.json",
              "workflows.json",
          ],
      },
      include_package_data=True,
)
