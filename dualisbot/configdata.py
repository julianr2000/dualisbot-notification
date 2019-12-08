import json

data = {}

def load_data(filename):
    with open(f'data/{filename}.json') as file:
        data[filename] = json.load(file)

load_data('config')
load_data('secrets')