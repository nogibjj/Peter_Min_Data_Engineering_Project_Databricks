"""Test goes here"""
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    test1 = extract()
    assert test1 is not None


def test_load():
    test2 = load()
    assert test2 == 'GradEmployment Database has been loaded or already created.'


def test_query():
    test3 = query()
    assert test3 == 'SQL query successfully executed.'


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()