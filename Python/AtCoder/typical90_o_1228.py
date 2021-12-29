from functools import lru_cache
# 差がk以上となるように、ボールをa個選ぶ
# a個のボールを選ぶ方法は
# (n-(k-1)*(a-1))_C_a
# aCb = a!/(b!(a-b)!)
# ある数pを選ぶと、次のk-1個は選べない、これがa-1回ある
mod = 10**9 + 7


def main():
    n = int(input())
    frac = [1]*(n+1)
    for i in range(2, n+1):
        frac[i] = (frac[i-1]*i) % mod
    ans_list = []

    for k in range(1, n+1):
        ans = 0
        for a in range(1, n+1):
            # k個間隔をあけて、a個選ぶ
            # k*(a-1)+1個のボールが必要
            # a = 2, k = 2だと、最低3つ必要で1通り
            # 3 - (2-1)*(2-1) = 2, 2C2 = 1
            if k*(a-1)+1 > n:
                break
            m = n-(k-1)*(a-1)
            r = a
            tmp = (frac[m]*rev_of(frac[r]) % mod)*rev_of(frac[m-r]) % mod
            ans += tmp
            ans %= mod
        ans_list.append(ans)
    print(*ans_list)


@lru_cache(maxsize=None)
def rev_of(val):
    return pow(val, mod-2, mod)


main()
