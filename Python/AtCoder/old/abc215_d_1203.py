# 素因数分解
# Aの素因数をすべて列挙して
# Aの素因数で割り切れないkをすべて列挙する
def main():
    _, m = map(int, input().split())
    A = list(map(int, input().split()))

    # 櫛
    n_end = 10**5+1
    is_prime = [True]*n_end
    is_prime[0] = is_prime[1] = False
    factor = [1]*n_end
    for n in range(1, n_end):
        if is_prime[n]:
            factor[n] = n
            for nn in range(n*n, n_end, n):
                is_prime[nn] = False
                factor[nn] = n

    # Aの素因数をすべて列挙
    factor_set = set()
    for a in A:
        while factor[a] != 1:
            factor_set.add(factor[a])
            a //= factor[a]

    # print(factor_set)
    ans = []

    for k in range(1, m+1):
        is_ans = True
        for factor in factor_set:
            if k % factor == 0:
                is_ans = False
                break
        if is_ans:
            ans.append(k)

    print(len(ans))
    print(*ans, sep='\n')


main()
