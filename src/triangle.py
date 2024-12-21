import math
def area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p*(p - a) * (p - b) * (p - c))


def perimeter(a, b, c):
    return a + b + c
