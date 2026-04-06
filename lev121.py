from fractions import Fraction #разложение цепных дробей

def continued_fraction(x, max_terms=20):
    cf = []
    f = Fraction(x)
    
    for _ in range(max_terms):
        a = f.numerator // f.denominator
        cf.append(a)
        
        remainder = f.numerator % f.denominator
        if remainder == 0:
            break
            
        f = Fraction(f.denominator, remainder)
    
    return cf

def evaluate(cf):
    if not cf:
        return Fraction(0)
    
    result = Fraction(cf[-1])
    for a in reversed(cf[:-1]):
        result = a + Fraction(1, result)
    
    return result

def to_string(cf):
    if len(cf) == 1:
        return str(cf[0])
    return f"[{cf[0]}; {', '.join(map(str, cf[1:]))}]"

if name == "main":
    print(to_string(continued_fraction(3.1415926535)))
    print(to_string(continued_fraction(22/7)))
    print(to_string(continued_fraction(2.71828)))
    print(float(evaluate(continued_fraction(3.1415926535))))