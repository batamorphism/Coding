from functools import lru_cache
import fractions


def main():
    _100_C_50 = factorial(100) // (factorial(50) * factorial(50))
    pow_2_100 = 2**100
    ans = fractions.Fraction(_100_C_50, pow_2_100)
    print(ans.numerator)
    print(ans.denominator)


def factorial(x):
    if x == 1:
        return 1
    return factorial(x-1)*x


main()
