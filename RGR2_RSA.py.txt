import math


# Расширенный алгоритм Евклида
def gcd_ext(a, b):
    if b == 0:
        return a, 1, 0

    d, x1, y1 = gcd_ext(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return d, x, y


# Нахождение обратного элемента
def get_inverse(e, phi):
    d, x, _ = gcd_ext(e, phi)

    if d != 1:
        return None

    return x % phi


# Шифрование символа
def rsa_encrypt(value, e, n):
    return pow(value, e, n)


# Дешифрование символа
def rsa_decrypt(value, d, n):
    return pow(value, d, n)


# Простые числа
p = 43
q = 47

print("\nЭТАП 1. Простые числа")
print(f"p = {p}")
print(f"q = {q}")

# Модуль RSA
n = p * q

print("\nЭТАП 2. Вычисление n")
print(f"n = {n}")

# Функция Эйлера
phi = (p - 1) * (q - 1)

print("\nЭТАП 3. Функция Эйлера")
print(f"φ(n) = {phi}")

# Открытая экспонента
e = 17

print("\nЭТАП 4. Открытый ключ")
print(f"e = {e}")

gcd_value = math.gcd(e, phi)

print(f"НОД({e}, {phi}) = {gcd_value}")

# Секретная экспонента
d = get_inverse(e, phi)

print("\nЭТАП 5. Закрытый ключ")
print(f"d = {d}")

print(f"Проверка:")
print(f"({e} * {d}) mod {phi} = {(e * d) % phi}")

# Ключи
print("\nКлючи RSA")
print(f"Открытый ключ : ({e}, {n})")
print(f"Закрытый ключ : ({d}, {n})")

# Исходное сообщение
text = "Четные числа - питательны, а нечетные - просто вкусные"

print("\nИсходная строка:")
print(text)

# Проверка размера n
max_symbol = max(ord(ch) for ch in text)

print("\nПроверка корректности n")
print(f"Максимальный код символа: {max_symbol}")
print(f"n = {n}")

if n > max_symbol:
    print("Размер n подходит")
else:
    print("n слишком маленькое")

# Шифрование
encrypted_data = []

print("\nЭТАП 6. Шифрование")
print(f"{'Символ':<10} {'Код':<10} {'Шифр'}")
print("-" * 35)

for symbol in text:

    code = ord(symbol)

    encrypted_code = rsa_encrypt(code, e, n)

    encrypted_data.append(encrypted_code)

    print(f"{repr(symbol):<10} {code:<10} {encrypted_code}")

# Дешифрование
decoded_chars = []

print("\nЭТАП 7. Дешифрование")
print(f"{'Шифр':<10} {'Код':<10} {'Символ'}")
print("-" * 35)

for item in encrypted_data:

    decoded_code = rsa_decrypt(item, d, n)

    decoded_symbol = chr(decoded_code)

    decoded_chars.append(decoded_symbol)

    print(f"{item:<10} {decoded_code:<10} {repr(decoded_symbol)}")

decoded_text = "".join(decoded_chars)

print("\nРезультат дешифрования:")
print(decoded_text)

print("\nПроверка:")

if decoded_text == text:
    print("Шифрование и дешифрование выполнены успешно")
else:
    print("Обнаружена ошибка")