#!/usr/bin/env python
# coding=utf-8

import requests
import pprint
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')
API_KEY = parser.get('apikeys', 'sunlightfoundationkey')

query_params = { 'apikey': 'API_KEY',
                 'entity_type': 'month',
                 'entity_value': '201210',
                 'phrase':'Top Words'}

endpoint = 'http://capitolwords.org/api/1/phrases.json'

response = requests.get(endpoint, params=query_params)
data = response.json()
print data
