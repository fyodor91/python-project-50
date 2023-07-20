def test_generate():
    result = '''{
    - follow:False
      host:hexlet.io
    - proxy:123.234.53.22
    - timeout:50
    + timeout:20
    + verbose:True
    }'''
    assert generate_diff(file1, file2) == result
