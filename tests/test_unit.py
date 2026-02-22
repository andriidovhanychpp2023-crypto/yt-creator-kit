# tests/test_unit.py
from src.logic import analyze_brainrot_title


def test_title_skibidi_rizz():
    # Класичний хайп
    assert analyze_brainrot_title("Skibidi Rizz Moment") == "BOP"


def test_title_ultra_rizz():
    # Поєднання сленгу та капсу
    assert analyze_brainrot_title("SIGMA GYATT") == "ULTRA RIZZ"


def test_title_boring():
    # Звичайна назва без сленгу
    assert analyze_brainrot_title("How to cook pasta") == "L TITLE"


def test_title_empty():
    # Порожній рядок
    assert analyze_brainrot_title("") == "Empty title"


def test_title_only_spaces():
    # Рядок з пробілів
    assert analyze_brainrot_title("   ") == "Empty title"


def test_title_case_insensitivity():
    # Перевірка, що регістр сленгу не має значення
    assert analyze_brainrot_title("sKiBiDi") == "BOP"


def test_title_just_caps_no_slang():
    # Капс без сленгу не дає ULTRA RIZZ
    assert analyze_brainrot_title("HELLO WORLD") == "L TITLE"
