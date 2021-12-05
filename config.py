import json

def read_config():
    with open('config.json') as f:
        json_data = json.load(f)
    return json_data

# print (read_config())
# print (type(read_config()))