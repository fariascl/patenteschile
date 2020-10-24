# patenteschile
Generador de patentes vehículares chilenas

patenteschile es una librería de Python que permite generar patentes vehiculares chilenas cumpliendo con la norma actual.

Uso:
```python
from patenteschile import Patente

patentes = Patente()
cant = 2 # cantidad de patentes
print(patentes.generate(cant))
```
