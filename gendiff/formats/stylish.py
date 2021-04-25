def stylish(source, offset=0):
    result = '{\n'
    keys = list(source.keys())
    keys.sort()
    for key in keys:
        result += make_string_from_key_with_flag(source[key], key, offset + 2)
    result += '}'
    return result


def make_string_from_key_with_flag(source_value, key, offset):
    flag = source_value.setdefault('flag', None)
    converted_flag = convert_flag(flag)
    if source_value['flag'] == 'dictionary':
        keys = list(source_value['children'].keys())
        keys.sort()
        temp_string = '  {}{}: {}\n'.format((offset * ' '), key, '{')
        for child in keys:
            temp_string += make_string_from_key_with_flag(
                source_value['children'][child], child, offset + 4)
        temp_string += '{}{}\n'.format((offset + 2) * ' ', '}')
        return temp_string
    if source_value['flag'] == 'updated':
        # return '{}{}'.format(source_value, key)
        return make_string_with_flag_updated(source_value, key, offset)
    if not isinstance(source_value['value'], dict):
        return '{}{} {}: {}\n'.format(
            (' ' * offset), converted_flag, key,
            convert_if_bool_or_none(source_value['value']))
    if flag == 'add' or flag == 'del' or flag == 'same':
        temp_string = '{}{} {}: {}\n'.format((offset * ' '),
                                             converted_flag, key, '{')
        temp_string += make_string_from_key_without_flag(
            convert_if_bool_or_none(source_value['value']), offset + 6)
        temp_string += '{}{}\n'.format((offset + 2) * ' ', '}')
        return temp_string


def make_string_with_flag_updated(source_value, key, offset):
    temp_string = ''
    old_value = convert_if_bool_or_none(source_value['old_value'])
    new_value = convert_if_bool_or_none(source_value['new_value'])
    for value_flag in [{'value': old_value, 'flag': '-'},
                       {'value': new_value, 'flag': '+'}]:
        if not isinstance(value_flag['value'], dict):
            temp_string += '{}{} {}: {}\n'.format(
                (' ' * offset), value_flag['flag'], key, value_flag['value'])
        else:
            temp_string += '{}{} {}: {}\n'.format(
                (offset * ' '), value_flag['flag'], key, '{')
            temp_string += make_string_from_key_without_flag(
                value_flag['value'], offset + 6)
            temp_string += '{}{}\n'.format((offset + 2) * ' ', '}')
    return temp_string


def make_string_from_key_without_flag(source_value, offset):
    temp_string = ''
    for key in source_value.keys():
        if not isinstance(source_value[key], dict):
            temp_string += '{}{}: {}\n'.format((' ' * offset),
                                               key, source_value[key])
        else:
            temp_string += '{}{}: {}\n'.format((offset * ' '), key, '{')
            temp_string += make_string_from_key_without_flag(
                convert_if_bool_or_none(source_value[key]), offset + 4)
            temp_string += '{}{}\n'.format(offset * ' ', '}')
    return temp_string


def convert_if_bool_or_none(value):
    res = value
    if value is False:
        res = 'false'
    if value is True:
        res = 'true'
    if value is None:
        res = 'null'
    return res


def convert_flag(flag):
    res = '  '
    if flag == 'add':
        res = '+'
    elif flag == 'del':
        res = '-'
    elif flag == 'same':
        res = ' '
    return res
