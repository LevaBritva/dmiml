import math

# Алгоритм Евклида (расширенный вариант)
def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0

    d, x1, y1 = gcd_extended(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return d, x, y


# Нахождение обратного элемента
def inverse_element(number, mod):
    d, x, _ = gcd_extended(number % mod, mod)

    if d != 1:
        return None

    return x % mod


# Решение одного линейного сравнения
def solve_linear_congruence(a, b, m):
    print(f"\nРешаем сравнение: {a}x ≡ {b} (mod {m})")

    d, _, _ = gcd_extended(a, m)

    if b % d != 0:
        print(f"НОД({a}, {m}) = {d}, решений нет")
        return None, None

    a_new = a // d
    b_new = b // d
    m_new = m // d

    print(f"После сокращения:")
    print(f"{a_new}x ≡ {b_new} (mod {m_new})")

    inv = inverse_element(a_new, m_new)

    x0 = (b_new * inv) % m_new

    print(f"Обратный элемент: {inv}")
    print(f"Частное решение: x ≡ {x0} (mod {m_new})")

    roots = [(x0 + k * m_new) % m for k in range(d)]

    return roots, m_new


# Объединение двух сравнений (КТО)
def combine_congruences(r1, m1, r2, m2):
    d, u, v = gcd_extended(m1, m2)

    if (r2 - r1) % d != 0:
        return None, None

    mod_result = (m1 * m2) // d

    value = (r1 + m1 * u * ((r2 - r1) // d)) % mod_result

    return value, mod_result


# Решение всей системы
def solve_congruence_system(system):
    print("\nРЕШЕНИЕ СИСТЕМЫ СРАВНЕНИЙ")

    print("\nИсходная система:")
    for index, (residue, mod) in enumerate(system, start=1):
        print(f"{index}) x ≡ {residue} (mod {mod})")

    print("\nПроверка совместности системы")

    for i in range(len(system)):
        for j in range(i + 1, len(system)):

            a1, m1 = system[i]
            a2, m2 = system[j]

            d = math.gcd(m1, m2)

            if (a2 - a1) % d != 0:
                print(f"Сравнения {i+1} и {j+1} несовместны")
                return None

    print("Система совместна")

    current_x, current_mod = system[0]
    current_x %= current_mod

    print("\nПоследовательно объединяем сравнения")

    for i in range(1, len(system)):

        next_x, next_mod = system[i]

        print("\nОбъединяем:")
        print(f"x ≡ {current_x} (mod {current_mod})")
        print(f"x ≡ {next_x} (mod {next_mod})")

        result_x, result_mod = combine_congruences(
            current_x,
            current_mod,
            next_x,
            next_mod
        )

        if result_x is None:
            print("Получена несовместная система")
            return None

        current_x = result_x
        current_mod = result_mod

        print(f"Новое сравнение:")
        print(f"x ≡ {current_x} (mod {current_mod})")

    print("\nОтвет:")
    print(f"x ≡ {current_x} (mod {current_mod})")
    print(f"x = {current_x} + {current_mod} * t")

    print("\nПроверка результата:")

    for residue, mod in system:
        check = current_x % mod

        print(
            f"{current_x} mod {mod} = {check} "
            f"(ожидалось {residue % mod})"
        )

    return current_x, current_mod


# Пример 1
print("\n===== ПРИМЕР 1 =====")
solve_congruence_system([
    (2, 3),
    (3, 5),
    (2, 7)
])

# Пример 2
print("\n===== ПРИМЕР 2 =====")
solve_congruence_system([
    (1, 4),
    (5, 6),
    (7, 10)
])

# Пример 3
print("\n===== ПРИМЕР 3 =====")
solve_congruence_system([
    (1, 4),
    (2, 6)
])