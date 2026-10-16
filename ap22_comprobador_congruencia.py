"""[AP 22] Comprobador de congruencia.

Curso de Seguridad Informática (MF0489).
Autor: Volodymyr Osebchuk.

Dos números enteros a y b son congruentes módulo n, y se escribe
a ≡ b (mod n), si al dividirlos entre n dan el mismo resto o,
de forma equivalente, si a - b es múltiplo de n.
"""


def son_congruentes(a, b, n):
    """Devuelve True si a ≡ b (mod n), es decir, si (a - b) es múltiplo de n.

    Lanza ValueError si el módulo n no es positivo.
    """
    if n <= 0:
        raise ValueError("El módulo n debe ser un entero positivo (n > 0).")
    return (a - b) % n == 0


def pedir_entero(mensaje):
    """Pide un número entero por teclado; lanza ValueError si no lo es."""
    return int(input(mensaje).strip())


def mostrar_resultado(a, b, n):
    """Muestra el resultado de la comprobación al estilo de la lección."""
    resto_a = a % n
    resto_b = b % n
    print()
    if son_congruentes(a, b, n):
        k = (a - b) // n
        print(f"{a} ≡ {b} (mod {n})")
        print(f"Porque {a} mod {n} = {resto_a} y {b} mod {n} = {resto_b}.")
        print(f"Además, {a} - {b} = {a - b} = {n} * ({k}), es múltiplo de {n}.")
    else:
        print(f"{a} ≢ {b} (mod {n})")
        print(f"Porque {a} mod {n} = {resto_a} y {b} mod {n} = {resto_b}: "
              "los restos son distintos.")
        print(f"Además, {a} - {b} = {a - b} no es múltiplo de {n}.")
    print()


def main():
    """Pide los datos al usuario y comprueba la congruencia."""
    print("=== Comprobador de congruencias: a ≡ b (mod n) ===")
    while True:
        try:
            a = pedir_entero("Introduce a: ")
            b = pedir_entero("Introduce b: ")
            n = pedir_entero("Introduce el módulo n: ")
            if n <= 0:
                raise ValueError
        except ValueError:
            print("Error: a, b y n deben ser números enteros y n debe ser mayor que 0.")
        else:
            mostrar_resultado(a, b, n)

        try:
            otra = input("¿Otra comprobación? (s/n): ").strip().lower()
        except EOFError:
            break
        if otra != "s":
            break
    print("Fin del programa.")


if __name__ == "__main__":
    main()
