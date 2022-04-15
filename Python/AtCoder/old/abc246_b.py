import math


def main():
    a, b = map(int, input().split())
    d = math.sqrt(a**2 + b**2)
    a /= d
    b /= d
    print(a, b)


main()
