import json

def obtain_credentials(filename, passname):
    with open(filename) as fn:
        data = json.load(fn)
    
    return data[passname]