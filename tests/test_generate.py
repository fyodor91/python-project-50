from gendiff.generate import generate_diff
from tests.fixtures.diff import true_result as result_1
from tests.fixtures.diff2 import true_result as result_2
import pytest
import json


def test_generate_json():
    file_1 = 'tests/fixtures/file1.json'
    file_2 = 'tests/fixtures/file2.json'
    assert generate_diff(file_1, file_2) == result_1


def test_generate_yaml():
    file_1 = 'tests/fixtures/file1.yml'
    file_2 = 'tests/fixtures/file2.yml'
    assert generate_diff(file_1, file_2) == result_1


def test_generate_json():
    file_3 = 'tests/fixtures/file3.json'
    file_4 = 'tests/fixtures/file4.json'
    assert generate_diff(file_3, file_4) == result_2


def test_generate_yaml():
    file_3 = 'tests/fixtures/file3.yml'
    file_4 = 'tests/fixtures/file4.yml'
    assert generate_diff(file_3, file_4) == result_2



