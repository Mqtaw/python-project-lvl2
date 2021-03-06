import yaml
import json


def parse(path_to_file):
    if path_to_file[-3:] == 'yml':
        return yaml.safe_load(open(path_to_file))
    elif path_to_file[-4:] == 'json':
        return json.load(open(path_to_file))
