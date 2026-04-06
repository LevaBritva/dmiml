from fractions import Fraction #диафантовые уравнения при помощи цепных дробей для любых чисел
from math import gcd

def continued_fraction(x):
    cf = []
    f = Fraction(x)
    for _ in range(100):
        a = f.numerator // f.denominator
        cf.append(a)
        r = f.numerator % f.denominator
        if r == 0:
            break
        f = Fraction(f.denominator, r)
    return cf

def convergents(cf):
    h = [0, 1]
    k = [1, 0]
    for a in cf:
        h.append(a * h[-1] + h[-2])
        k.append(a * k[-1] + k[-2])
    return zip(h[2:], k[2:])

def solve_diophantine(a, b, c):
    g = gcd(a, b)
    if c % g != 0:
        return None
    
    cf = continued_fraction(Fraction(a, b))
    for p, q in convergents(cf):
        if a * q - b * p == g or a * q - b * p == -g:
            x = q * (c // g)
            y = -p * (c // g)
            if a * q - b * p == -g:
                x = -x
                y = -y
            return x, y, g
    return None

print(solve_diophantine(15, 26, 1))
print(solve_diophantine(123, 45, 30))
print(solve_diophantine(7, 5, 3))
print(solve_diophantine(8, 5, 1))