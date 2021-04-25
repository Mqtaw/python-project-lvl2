def plain(source):
    # print(source)
    result = make_plain_response(source)
    return result[:-1]


def make_plain_response(source, upper_key=None):
    result = ''
    keys = list(source.keys())
    keys.sort()
    for num, key in enumerate(keys):
        flag = source[key].setdefault('flag', None)
        if upper_key is None:
            temp_string = make_string_from_key_with_flag(source[key], key)
        else:
            temp_string = make_string_from_key_with_flag(
                source[key], '{}.{}'.format(upper_key, key))
        if temp_string:
            result += temp_string
            if flag != 'dictionary':
                result += '\n'
    return result


def make_string_from_key_with_flag(source_value, key=None):
    if source_value['flag'] == 'dictionary':
        return make_plain_response(source_value['children'], key)
    if source_value['flag'] == 'add':
        return 'Property \'{}\' was added with value: {}'.format(
            key, convert_value(source_value['value']))
    if source_value['flag'] == 'del':
        return 'Property \'{}\' was removed'.format(key)
    if source_value['flag'] == 'updated':
        old_value = convert_value(source_value['old_value'])
        new_value = convert_value(source_value['new_value'])
        return 'Property \'{}\' was updated. From {} to {}'.format(
            key, old_value, new_value)


def convert_value(value):
    res = '\'{}\''.format(value)
    if isinstance(value, int):
        res = value
    if value is False:
        res = 'false'
    if value is True:
        res = 'true'
    if value is None:
        res = 'null'
    if isinstance(value, dict):
        res = '[complex value]'
    return res
