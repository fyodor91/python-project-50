from gendiff.generate import generate_diff
from tests.fixtures.diff import true_result
import pytest
import json


def test_generate_diff():
    file_1 = 'tests/fixtures/file1.json'
    file_2 = 'tests/fixtures/file2.json'
    assert generate_diff(file_1, file_2) == true_result
