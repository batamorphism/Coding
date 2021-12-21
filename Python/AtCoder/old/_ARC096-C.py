import math


def main():
    a, b, c, x, y = map(int, input().split())
    ans = 10**10
    for c_count in range(max(x, y)*2+1):
        a_count = max(x-math.floor(c_count/2), 0)
        b_count = max(y-math.floor(c_count/2), 0)
        ans = min(ans, a*a_count+b*b_count+c*c_count)

    print(ans)


main()
