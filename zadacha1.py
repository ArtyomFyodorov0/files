from fractions import Fraction
from sympy import Symbol, gcd, Poly

class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        coeffs1 = self.coeffs + [0] * (max_len - len(self.coeffs))
        coeffs2 = other.coeffs + [0] * (max_len - len(other.coeffs))
        return Polynomial([a + b for a, b in zip(coeffs1, coeffs2)])

    def evaluate(self, x):
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x**i)
        return result

    def derivative(self):
        if not self.coeffs:
            return Polynomial([])
        derived_coeffs = [i * c for i, c in enumerate(self.coeffs[1:], 1)]
        return Polynomial(derived_coeffs)

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            polynomial_str = ""
            for i, coeff in enumerate(self.coeffs):
                if coeff == 0:
                    continue
                if coeff > 0 and i > 0:
                    polynomial_str += "+"
                polynomial_str += str(coeff)
                if i > 0:
                    polynomial_str += "x"
                    if i > 1:
                        polynomial_str += "^" + str(i)
            f.write(polynomial_str + "\n")

    def find_integer_roots(self):
        if not all(isinstance(c, Fraction) for c in self.coeffs):
            raise ValueError("All coefficients must be Fractions to find integer roots.")
        roots = []
        for i in range(-10, 11): #Проверка ограниченного диапазона
            if self.evaluate(i) == 0:
                roots.append(i)
        return roots

    def to_sympy_poly(self, x):
        return Poly(self.coeffs, x)

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coeffs):
            if coeff == 0: continue
            if coeff == 1 and i > 0: coeff_str = ""
            elif coeff == -1 and i > 0: coeff_str = "-"
            else: coeff_str = str(coeff)
            if i == 0:
                terms.append(coeff_str)
            elif i == 1:
                terms.append(f"{coeff_str}x")
            else:
                terms.append(f"{coeff_str}x^{i}")
        return " + ".join(terms) or "0"



def polynomial_gcd(p1, p2):
    x = Symbol('x')
    return gcd(p1.to_sympy_poly(x), p2.to_sympy_poly(x))


# Пример использования:
p1 = Polynomial([1, -2, 1])  # x^2 - 2x + 1
p2 = Polynomial([Fraction(1, 2), -1, Fraction(1, 2)])  # (1/2)x^2 - x + (1/2)

print(f"p1: {p1}")
print(f"p2: {p2}")

p3 = p1 + p2
print(f"p1 + p2: {p3}")

print(f"p1(2) = {p1.evaluate(2)}")

p1_derivative = p1.derivative()
print(f"Производная p1: {p1_derivative}")

p1.write_to_file("polynomial1.txt")


try:
    integer_roots_p2 = p2.find_integer_roots()
    print(f"Целые корни p2: {integer_roots_p2}")
except ValueError as e:
    print(f"Ошибка при поиске целых корней p2: {e}")

gcd_result = polynomial_gcd(p1,p2)
print(f"НОД(p1, p2) : {gcd_result}") #Вывод в формате sympy

gcd_coeffs = gcd_result.all_coeffs()
gcd_poly_custom = Polynomial(gcd_coeffs)
print(f"НОД(p1, p2) : {gcd_poly_custom}") #Вывод в привычном формате
