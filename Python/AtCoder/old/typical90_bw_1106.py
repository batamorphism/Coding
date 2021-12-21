import math

def main():
    x = int(input())
    # xを素因数分解
    m = int(x**0.5) + 10
    factor = []
    for num in range(2, m):
        while x % num == 0:
            # numはxの素因数
            factor.append(num)
            x //= num

    if x > 1:
        factor.append(x)

    factor_len = len(factor)
    # 魔法を一回使うごとに、factorの要素数を半分にすることができる
    cnt = 0
    while factor_len != 1:
        cnt += 1
        factor_len = math.ceil(factor_len / 2)

    print(cnt)


main()
