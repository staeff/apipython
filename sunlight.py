#!/usr/bin/env python
# coding=utf-8

import requests
import pprint
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')
API_KEY = parser.get('apikeys', 'sunlightfoundationkey')

query_params = { 'apikey': 'API_KEY',
                 'per_page': 3,
                 'state': 'MD',
                 'phrase': 'election night'}

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get(endpoint, params=query_params)

data = response.json()
pprint.pprint(data)
