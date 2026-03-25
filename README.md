# patenteschile

Generador y validador de patentes vehiculares chilenas.

patenteschile es una librería de Python que permite generar y validar patentes vehiculares chilenas cumpliendo con la norma actual y las antiguas.

## Instalación

```bash
pip install patenteschile
```

## Uso

### Generar patentes

```python
from patenteschile import Patente

p = Patente()

# Auto actual (4 letras + 2 números)
p.generate(5)
# ['TXGV97', 'BKPL28', 'ZWXY99', ...]

# Moto actual (2 letras + 3 números)
p.generate(5, vehicle_type="moto")
# ['BK123', 'CD999', 'FG456', ...]

# Auto antiguo (2 letras + 4 números)
p.generate(5, system="old")
# ['AB1234', 'AE5678', 'XY9876', ...]

# Moto antigua
p.generate(5, system="old", vehicle_type="moto")

# Remolque liviano antiguo (< 3860 kg)
p.generate(5, system="old", vehicle_type="remolque_liviano")

# Remolque pesado antiguo (> 3860 kg)
p.generate(5, system="old", vehicle_type="remolque_pesado")
```

### Validar patentes

```python
from patenteschile import Patente

p = Patente()

# Validar cualquier formato
p.validate("TXGV97")   # True (auto actual)
p.validate("AB1234")  # True (auto antiguo)
p.validate("BK123")   # True (moto actual/antigua)

# Patentes inválidas
p.validate("AAAB12")   # False (tiene vocal)
p.validate("AÑ1234")   # False (tiene Ñ bloqueada)
p.validate("AQ1234")   # False (tiene Q bloqueada)
p.validate("invalid")  # False
```

## Formatos soportados

| Sistema | Vehículo | Formato | Letras permitidas |
|---------|----------|---------|-------------------|
| Actual | Auto | XXXXNN | 18 consonantes (sin vocales, M, N, Ñ, O, Q, U) |
| Actual | Moto | XXNNN | 18 consonantes |
| Antiguo | Auto | AANNNN | Todas excepto Ñ, Q |
| Antiguo | Moto | XXNNN | 18 consonantes |
| Antiguo | Remolque liviano | AANNNN | Todas excepto Ñ, Q |
| Antiguo | Remolque pesado | AANNNN | Todas excepto Ñ, Q |

## Licencia

MIT
