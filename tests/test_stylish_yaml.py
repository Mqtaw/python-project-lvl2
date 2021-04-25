from gendiff.gendiff import generate_diff


def test():
    with open('tests/fixtures/stylish_resp') as f:
        response = f.read()
        f.close()
        print(response)
    assert generate_diff('tests/fixtures/file1.yml',
                         'tests/fixtures/file2.yml') == response
