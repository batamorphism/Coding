import math


def main():
    a, b, x = map(int, input().split())
    x = x/a
    if x >= a*b/2:
        h = (a*b-x)/a*2
        theta = math.atan(h/a)
        ans = math.degrees(theta)
    else:
        h = x/b*2
        theta = math.atan(b/h)
        ans = math.degrees(theta)
    print(ans)


main()
