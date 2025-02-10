from pprint import pprint

import requests


search_name = 'Luke Skywalker'
response = requests.get(
    f'https://swapi.dev/api/people?search={search_name}'
    ).json()

pprint(response.get('results')[0])
