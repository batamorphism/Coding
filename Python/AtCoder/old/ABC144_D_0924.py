import math

def main():
    a, b, x = map(int, input().split())
    h = x/a**2
    if h >= b/2:
        # 側面の面積をmとする
        # m = (k+b)/2*a
        # m = a*h より
        k = 2*h-b
        # tan(theta) = (b-k)/a
        # theta = atan((b-k)/a)
        theta = math.atan((b-k)/a)
        ans = math.degrees(theta)
    else:
        # m = k*b/2
        k = a*h*2/b
        # tan(theta) = b/k
        theta = math.atan(b/k)
        ans = math.degrees(theta)
    print(ans)


main()
