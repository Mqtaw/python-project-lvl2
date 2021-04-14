import argparse
from gendiff.parse import parse


def createParser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser


def generate_diff(path_to_file1, path_to_file2):
    differences = ''
    file1 = parse(path_to_file1)
    file2 = parse(path_to_file2)
    keys = list(file1.keys() | file2.keys())
    keys.sort()
    for key in keys:
        differences += add_string_to_differences(file1, file2, key)
        if key != keys[-1]:
            differences += '\n'
    return differences


def add_string_to_differences(file1, file2, key):
    if key in file1 and key not in file2:
        return '- {}: {}'.format(key, file1[key])
    elif key in file1 and key in file2 and file1[key] == file2[key]:
        return '  {}: {}'.format(key, file1[key])
    elif key in file1 and key in file2 and file1[key] != file2[key]:
        temp = '- {}: {}\n'.format(key, file1[key])
        temp += '+ {}: {}'.format(key, file2[key])
        return temp
    elif key not in file1 and key in file2:
        return '+ {}: {}'.format(key, file2[key])
