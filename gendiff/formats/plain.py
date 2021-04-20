def plain(source):
    # print(source)
    result = ''
    keys = list(source.keys())
    keys.sort()
    for key in keys:
        temp_string = make_string_from_key_with_flag(source[key], key)
        if temp_string:
            result += temp_string
    return result


def make_string_from_key_with_flag(source_value, key):
    # flag = source_value.setdefault('flag', None)
    if source_value['flag'] == 'dictionary':
        keys = list(source_value['children'].keys())
        keys.sort()
        temp_string = ''
        for child in keys:
            temp_string_deeper = make_string_from_key_with_flag(
                source_value['children'][child], '{}.{}'.format(key, child))
            if temp_string_deeper:
                temp_string += temp_string_deeper
        return temp_string
    if source_value['flag'] == 'add':
        return '\nProperty \'{}\' was added with value: {}'.format(
            key, convert_value(source_value['value']))
    if source_value['flag'] == 'del':
        return '\nProperty \'{}\' was removed'.format(key)
    if source_value['flag'] == 'updated':
        old_value = convert_value(source_value['old_value'])
        new_value = convert_value(source_value['new_value'])
        return '\nProperty \'{}\' was updated. From {} to {}'.format(
            key, old_value, new_value)


def convert_value(value):
    if value is False:
        return 'false'
    if value is True:
        return 'true'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    return '\'{}\''.format(value)
