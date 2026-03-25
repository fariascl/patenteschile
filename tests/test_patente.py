import pytest
from patenteschile import Patente


class TestGenerate:
    def test_generate_auto_current(self):
        p = Patente()
        result = p.generate(5)
        assert len(result) == 5
        for patente in result:
            assert len(patente) == 7
            letters = patente[:-3]
            assert all(c in p.CURRENT_CONSONANTS for c in letters)
            assert int(patente[-2:]) in range(10, 100)

    def test_generate_moto_current(self):
        p = Patente()
        result = p.generate(5, vehicle_type="moto")
        assert len(result) == 5
        for patente in result:
            assert len(patente) == 6

    def test_generate_auto_old(self):
        p = Patente()
        result = p.generate(5, system="old")
        assert len(result) == 5

    def test_generate_moto_old(self):
        p = Patente()
        result = p.generate(5, system="old", vehicle_type="moto")
        assert len(result) == 5

    def test_generate_remolque_liviano_old(self):
        p = Patente()
        result = p.generate(5, system="old", vehicle_type="remolque_liviano")
        assert len(result) == 5

    def test_generate_remolque_pesado_old(self):
        p = Patente()
        result = p.generate(5, system="old", vehicle_type="remolque_pesado")
        assert len(result) == 5


class TestValidate:
    def test_validate_auto_current_valid(self):
        p = Patente()
        assert p.validate("TXGV-97") is True
        assert p.validate("BKPL-28") is True
        assert p.validate("ZWXY-99") is True

    def test_validate_auto_current_invalid_letters(self):
        p = Patente()
        assert p.validate("AAAB-12") is False
        assert p.validate("TXEV-97") is False

    def test_validate_auto_current_invalid_numbers(self):
        p = Patente()
        assert p.validate("TXGV-09") is False
        assert p.validate("TXGV-00") is False

    def test_validate_auto_old_valid(self):
        p = Patente()
        assert p.validate("AB-1234") is True
        assert p.validate("AE-5678") is True

    def test_validate_auto_old_invalid_blocked(self):
        p = Patente()
        assert p.validate("AÑ-1234") is False
        assert p.validate("AQ-1234") is False

    def test_validate_moto_current_valid(self):
        p = Patente()
        assert p.validate("BK-123") is True
        assert p.validate("CD-999") is True

    def test_validate_moto_current_invalid(self):
        p = Patente()
        assert p.validate("AA-123") is False
        assert p.validate("AB-1234") is True

    def test_validate_moto_old_valid(self):
        p = Patente()
        assert p.validate("BK-123") is True
        assert p.validate("CD-999") is True

    def test_validate_invalid_format(self):
        p = Patente()
        assert p.validate("AAAAAAAA-99") is False
        assert p.validate("AB") is False
        assert p.validate("") is False
