#!/usr/bin/env python
# coding=utf-8

import requests
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

API_KEY = parser.get('apikeys', 'giantbombkey')

query_params = {'sort': 'release_date:desc',
                'api_key': API_KEY,
                'field_list':
                'release_date,original_price,name,abbreviation',
                'format': 'json'}

endpoint = 'http://www.giantbomb.com/api/platforms/'

response = requests.get(endpoint, params=query_params)
print response

data = response.json()
print(data)
