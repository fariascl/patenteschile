#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from patenteschile import Patente


def test_all():
    p = Patente()
    passed = 0
    failed = 0

    def assert_test(condition, test_name):
        nonlocal passed, failed
        if condition:
            print(f"✓ {test_name}")
            passed += 1
        else:
            print(f"✗ {test_name}")
            failed += 1

    print("=== GENERATE ===\n")

    print("Auto actual:")
    autos = p.generate(3)
    print(f"  {autos}")
    assert_test(len(autos) == 3, "generate auto actual")

    print("\nMoto actual:")
    motos = p.generate(3, vehicle_type="moto")
    print(f"  {motos}")
    assert_test(len(motos) == 3, "generate moto actual")

    print("\nAuto antiguo:")
    autos_old = p.generate(3, system="old")
    print(f"  {autos_old}")
    assert_test(len(autos_old) == 3, "generate auto old")

    print("\nMoto antigua:")
    motos_old = p.generate(3, system="old", vehicle_type="moto")
    print(f"  {motos_old}")
    assert_test(len(motos_old) == 3, "generate moto old")

    print("\nRemolque liviano antiguo:")
    remol_liv = p.generate(3, system="old", vehicle_type="remolque_liviano")
    print(f"  {remol_liv}")
    assert_test(len(remol_liv) == 3, "generate remolque liviano")

    print("\nRemolque pesado antiguo:")
    remo_pes = p.generate(3, system="old", vehicle_type="remolque_pesado")
    print(f"  {remo_pes}")
    assert_test(len(remo_pes) == 3, "generate remolque pesado")

    print("\n=== VALIDATE ===\n")

    assert_test(p.validate("TXGV97") is True, "validate auto actual valida")
    assert_test(p.validate("BKPL28") is True, "validate auto actual valida 2")
    assert_test(p.validate("AAAB12") is False, "validate auto actual con vocal")
    assert_test(p.validate("TXGV09") is False, "validate auto actual numero < 10")

    assert_test(p.validate("AB1234") is True, "validate auto old valida")
    assert_test(p.validate("AE5678") is True, "validate auto old con vocal")
    assert_test(p.validate("AÑ1234") is False, "validate auto old con Ñ bloqueada")
    assert_test(p.validate("AQ1234") is False, "validate auto old con Q bloqueada")

    assert_test(p.validate("BK123") is True, "validate moto actual valida")
    assert_test(p.validate("AA123") is False, "validate moto actual con vocal")

    assert_test(p.validate("AAAAAAAA99") is False, "validate formato invalido")
    assert_test(p.validate("") is False, "validate vacio")

    print(f"\n=== RESULTADO: {passed} passed, {failed} failed ===")
    return failed == 0


if __name__ == "__main__":
    success = test_all()
    sys.exit(0 if success else 1)
