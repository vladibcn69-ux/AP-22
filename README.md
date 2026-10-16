# [AP 22] Comprobador de congruencia

Curso de Seguridad Informática (MF0489). Autor: Volodymyr Osebchuk.

## Descripción

Programa en Python que pide tres datos (a, b y el módulo n) y determina
matemáticamente si existe congruencia a ≡ b (mod n).

## Teoría

Dos números enteros a y b están en la misma clase de congruencia módulo n
si al dividirlos entre n dan el mismo resto o, de forma equivalente, si
a - b es múltiplo de n. Se escribe a ≡ b (mod n) (notación de Gauss).

Ejemplo de la lección: 63 ≡ 83 (mod 10), porque 63 mod 10 = 3 y
83 mod 10 = 3; además 63 - 83 = -20 = 10 * (-2).

## Archivos

| Archivo | Descripción |
|---|---|
| `ap22_comprobador_congruencia.py` | Programa principal (`son_congruentes` y `main`) |
| `test_ap22.py` | Pruebas unitarias con `unittest` |
| `.gitignore` | Archivos ignorados por Git |

## Cómo ejecutar

```
python ap22_comprobador_congruencia.py
python -m unittest
```

Solo se usa la biblioteca estándar de Python 3.

## Ejemplo de salida

```
=== Comprobador de congruencias: a ≡ b (mod n) ===
Introduce a: 63
Introduce b: 83
Introduce el módulo n: 10

63 ≡ 83 (mod 10)
Porque 63 mod 10 = 3 y 83 mod 10 = 3.
Además, 63 - 83 = -20 = 10 * (-2), es múltiplo de 10.

¿Otra comprobación? (s/n): s
Introduce a: 63
Introduce b: 84
Introduce el módulo n: 10

63 ≢ 84 (mod 10)
Porque 63 mod 10 = 3 y 84 mod 10 = 4: los restos son distintos.
Además, 63 - 84 = -21 no es múltiplo de 10.

¿Otra comprobación? (s/n): n
Fin del programa.
```
