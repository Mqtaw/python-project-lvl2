import argparse
from gendiff.parse import parse
from gendiff.formats.stylish import stylish
from gendiff.formats.plain import plain
from gendiff.formats.json import json_string


def createParser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    return parser


def check_format(format):
    if format == 'stylish':
        return stylish
    if format == 'plain':
        return plain
    if format == 'json':
        return json_string


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    file1 = parse(path_to_file1)
    file2 = parse(path_to_file2)
    f = check_format(format)
    return f(get_dif(file1, file2))


def get_dif(dict1, dict2):
    dif_dict = {}
    for key in (dict1.keys() | dict2.keys()):
        dif_dict[key] = make_item_for_dif_dict(
            dict1.setdefault(key, 'no such key'),
            dict2.setdefault(key, 'no such key'))
    return dif_dict


def make_item_for_dif_dict(dict1_item, dict2_item):
    if isinstance(dict1_item, dict) and isinstance(dict2_item, dict):
        return {'flag': 'dictionary',
                'children': get_dif(dict1_item, dict2_item)}
    elif dict1_item != 'no such key' and dict2_item == 'no such key':
        return {'flag': 'del', 'value': dict1_item}
    elif dict1_item == 'no such key' and dict2_item != 'no such key':
        return {'flag': 'add', 'value': dict2_item}
    elif dict1_item == dict2_item:
        return {'flag': 'same', 'value': dict1_item}
    elif dict1_item != dict2_item:
        return {'flag': 'updated', 'old_value': dict1_item,
                'new_value': dict2_item}
