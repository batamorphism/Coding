from functools import lru_cache
mod = 10**9 + 7


# kがでかくなると組み合わせ数は小さくなる
# n個から、差がk以上となるように選ぶ組み合わせ数をf(n, k)とする
# これは、幅nの区間に、幅kのマスを埋め込む方法が何通りあるか
# 幅nの区間に、幅kのマスを、x個埋め込む方法を考える
# このxが急速に減少していくので、間に合う
def main():
    n = int(input())
    ans = 0
    frac = [1]*(n+10)
    for i in range(1, n+10):
        frac[i] = i*frac[i-1]
        frac[i] %= mod

    for k in range(1, n+1):
        ans = 0
        for x in range(1, n+1):
            # 必要なマスの数は、k*(x-1)+1
            if k*(x-1)+1 > n:
                break
            # 自由度は、n-k*(x-1)
            # ここからk個選ぶ
            a = n - (k*(x-1)+1) + x
            r = x
            # print(a, r)
            # aCr = a!/(r!(a-r)!)
            val = frac[a] * rev(frac[r]) * rev(frac[a-r])
            ans += val
            ans %= mod
        print(ans % mod)


@lru_cache(maxsize=None)
def rev(a):
    return pow_mod(a, mod-2)


@lru_cache(maxsize=None)
def pow_mod(a, b):
    return pow(a, b, mod)


main()
