from contohji import hitung_total
import pytest

def test_penjumlahan_integer():
    assert hitung_total(5, 3) == 8

def test_penjumlahan_negatif():
    assert hitung_total(-2, -4) == -6

def test_penjumlahan_nol():
    assert hitung_total(0, 0) == 0

def test_penjumlahan_float():
    with pytest.raises(TypeError):
        hitung_total(3.5, 2.5)