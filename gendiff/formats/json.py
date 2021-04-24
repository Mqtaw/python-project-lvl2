import json


def json_string(source):
    return (json.dumps(add_flagtokey_to_source(source),
                       sort_keys=True, indent=2))


def add_flagtokey_to_source(source):
    result = {}
    for key in source.keys():
        converted_flag = convert_flag(source[key]['flag'])
        if source[key]['flag'] == 'add' or source[key]['flag'] == 'del' or\
                source[key]['flag'] == 'updated':
            value = source[key]['value'] if \
                source[key]['flag'] != 'updated' else source[key]['new_value']
            result['{} {}'.format(converted_flag, key)] = value
        if source[key]['flag'] == 'dictionary':
            result['{}'.format(key)] = add_flagtokey_to_source(
                source[key]['children'])
    return result


def convert_flag(flag):
    res = ''
    if flag == 'add':
        res = '+'
    elif flag == 'del':
        res = '-'
    elif flag == 'updated':
        res = '(upd)'
    return res
