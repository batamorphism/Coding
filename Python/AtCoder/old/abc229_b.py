def main():
    a, b = map(int, input().split())
    c = a+b
    # 繰り上がりなしで計算した物をdとする
    d = 0
    p = 1
    while not(a == 0 and b == 0):
        d += p * (((a % 10) + (b % 10)) % 10)
        a //= 10
        b //= 10
        p *= 10
    if c == d:
        print('Easy')
    else:
        print('Hard')


main()
