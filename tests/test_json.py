from gendiff.gendiff import generate_diff


def test():
    with open('tests/fixtures/json_resp.txt') as f:
        response = f.read()
        f.close()
        print(response)
    assert generate_diff('tests/fixtures/file_r1.yml',
                         'tests/fixtures/file_r2.yml',
                         format='json') == response
