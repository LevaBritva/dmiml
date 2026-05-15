from itertools import product

def zhegalkin_polynomial(func):
    """
    Строит полином Жигалкина для булевой функции двух переменных.

    func(x, y) -> 0 или 1
    """

    values = [
        func(0, 0),
        func(0, 1),
        func(1, 0),
        func(1, 1)
    ]

    # Коэффициенты полинома Жигалкина
    a0 = values[0]
    a1 = values[0] ^ values[2]
    a2 = values[0] ^ values[1]
    a12 = values[0] ^ values[1] ^ values[2] ^ values[3]

    terms = []

    if a0:
        terms.append("1")
    if a1:
        terms.append("x")
    if a2:
        terms.append("y")
    if a12:
        terms.append("xy")

    polynomial = " ⊕ ".join(terms) if terms else "0"

    return {
        "truth_table": values,
        "coefficients": {
            "1": a0,
            "x": a1,
            "y": a2,
            "xy": a12
        },
        "polynomial": polynomial
    }


#  Пример 
# Функция XOR
def f(x, y):
    return x ^ y


result = zhegalkin_polynomial(f)

print("Таблица истинности:", result["truth_table"])
print("Коэффициенты:", result["coefficients"])
print("Полином Жигалкина:", result["polynomial"])