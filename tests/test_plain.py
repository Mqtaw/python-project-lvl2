from gendiff.gendiff import generate_diff


def test():
    with open('tests/fixtures/plain_resp.txt') as f:
        response = f.read()
        f.close()
        print(response)
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', format='plain') == response



