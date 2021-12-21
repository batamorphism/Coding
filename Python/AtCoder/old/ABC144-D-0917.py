import math


def main():
    a, b, x = map(int, input().split())
    theta = 0
    half = a*a*b/2
    if x >= half:
        h = 2*x/(a**2)-b
        theta = math.degrees(math.atan((b-h)/a))
    else:
        # もっと斜めになる場合
        h = 2*x/(a*b)
        theta = math.degrees(math.atan(b/h))

    print(theta)


main()
