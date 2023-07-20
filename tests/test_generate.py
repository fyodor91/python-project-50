from gendiff.generate import generate_diff
import pytest


def main():
    file_1 = 'gendiff/files/file1.json'
    file_2 = 'gendiff/files/file2.json'
    result = '''{
    - follow:False
      host:hexlet.io
    - proxy:123.234.53.22
    - timeout:50
    + timeout:20
    + verbose:True
    }'''
    assert generate_diff(file_1, file_2) == result
