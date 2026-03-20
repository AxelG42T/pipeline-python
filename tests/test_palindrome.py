import pytest
from src.palindrome import est_palindrome
import pylint

def test_est_palindrome_vide():
    assert est_palindrome("") == True

def test_est_palindrome_une_lettre():
    assert est_palindrome("a") == True

def test_est_palindrome_palindrome_simple():
    assert est_palindrome("radar") == True

def test_est_palindrome_non_palindrome():
    assert est_palindrome("hello") == False

def test_est_palindrome_avec_espaces():
    assert est_palindrome("a man a plan a canal panama") == True

def test_est_palindrome_casse_insensible():
    assert est_palindrome("Radar") == True

def test_est_palindrome_phrase_non_palindrome():
    assert est_palindrome("Bonjour le monde") == False

def test_est_palindrome_nombres():
    assert est_palindrome("12321") == True

def test_est_palindrome_nombres_non_palindrome():
    assert est_palindrome("12345") == False
