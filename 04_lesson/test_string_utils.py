import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("скайпро", "Скайпро"),
    ("привет мир", "Привет мир")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("567", "567")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" hello", "hello"),
    (" ", ""),
    (" привет", "привет"),
    (" 456", "456"),
    (" привет мир", "привет мир")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("hello ", "hello "),
    ("привет мир", "привет мир"),
    ("", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("hello", "h", True),
    ("привет", "р", True),
    ("456", "5", True),
    ("привет мир", "м", True),
    ("lesson", "a", False),
    ("урок", "в", False)
])
def test_contains_positive(input_str, simbol, expected):
    assert string_utils.contains(input_str, simbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("", "h", False),
    (" ", "р", False)
])
def test_contains_negative(input_str, simbol, expected):
    assert string_utils.contains(input_str, simbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("hello", "l", "heo"),
    ("привет", "вет", "при"),
    ("987", "7", "98")
])
def test_delete_symbol_positive(input_str, simbol, expected):
    assert string_utils.delete_symbol(input_str, simbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, simbol, expected", [
    ("lesson", "a", "lesson"),
    (" ", "h", " ")
])
def test_delete_symbol_negative(input_str, simbol, expected):
    assert string_utils.delete_symbol(input_str, simbol) == expected
