import json


def json_string(source):
    return (json.dumps(add_flagtokey_to_source(source),
                       sort_keys=True, indent=2))


def add_flagtokey_to_source(source):
    result = {}
    for key in source.keys():
        if source[key]['flag'] == 'add':
            result['+ {}'.format(key)] = source[key]['value']
        if source[key]['flag'] == 'del':
            result['- {}'.format(key)] = source[key]['value']
        if source[key]['flag'] == 'updated':
            result['(upd) {}'.format(key)] = source[key]['new_value']
            # result['+ {}'.format(key)] = source[key]['new_value']
        if source[key]['flag'] == 'dictionary':
            result['{}'.format(key)] = add_flagtokey_to_source(
                source[key]['children'])
    return result
