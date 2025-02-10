from pprint import pprint

import requests


search_name = 'Luke Skywalker'
response = requests.get(
    f'https://swapi.dev/api/people?search={search_name}'
    ).json()
homeword_planet_url = str(response.get('results')[0].get('homeworld'))
response_for_planet_detail = requests.get(homeword_planet_url).json()
diameter = int(response_for_planet_detail.get('diameter'))

pprint(diameter)
