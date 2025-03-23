import pytest # noqa
from string_utils import StringUtils

# Инициализация объекта для тестирования
string_utils = StringUtils()

# Тесты для функции capitalize


def test_capitalize_positive():
    assert string_utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty_string():
    assert string_utils.capitalize("") == ""


def test_capitalize_already_capitalized():
    assert string_utils.capitalize("Skypro") == "Skypro"

# Тесты для функции trim


def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert string_utils.trim("skypro") == "skypro"


def test_trim_all_spaces():
    assert string_utils.trim("     ") == ""

# Тесты для функции contains


def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") is True


def test_contains_negative():
    assert string_utils.contains("SkyPro", "U") is False


def test_contains_empty_string():
    assert string_utils.contains("", "S") is False

# Тесты для функции delete_symbol


def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring():
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"


def test_delete_symbol_empty_string():
    assert string_utils.delete_symbol("", "S") == ""
