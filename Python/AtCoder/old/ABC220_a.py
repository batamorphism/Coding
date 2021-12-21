import math

def main():
    a, b, c = map(int, input().split())
    k = math.ceil(a/c)
    ans = k*c
    if ans > b:
        print(-1)
    else:
        print(ans)


main()
