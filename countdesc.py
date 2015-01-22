#!/usr/bin/env python
# coding=utf-8

import requests
import pprint
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')
API_KEY = parser.get('apikeys', 'sunlightfoundationkey')

query_params = { 'apikey': API_KEY,
				 'per_page': 10,
				 'entity_type': 'month',
				 'entity_value': '201210',
				 'sort': 'count desc'
		 		}

endpoint = 'http://capitolwords.org/api/1/phrases.json'

#import ipdb; ipdb.set_trace()
response = requests.get(endpoint, params=query_params)
print response

data = response.json()
# pprint.pprint(data)
