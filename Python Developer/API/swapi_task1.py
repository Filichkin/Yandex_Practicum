from pprint import pprint

import requests


response = requests.get('https://swapi.dev/api/people/').json()
characters = response['results']

pprint(characters)
