import json

def read_config():
    with open('config.json') as f:
        data = json.load(f)
    return data

# print (read_config())
# print (type(read_config()))