mod = 10**9+7


def calc(n):
    # x = 1, ..., nについて、整数xをx回書く
    ans = 0
    # nを下回る、10**k-1を求める
    k = 0
    while 10**k - 1 <= n:
        k += 1
    k -= 1
    # 1～999...999については、文字は10**k-1回出てくる
    for deg in range(1, k+1):
        # deg桁について、それぞれ10**(deg-1)～10**deg-1の総和を求め、deg倍する
        lo = 10**(deg-1)
        hi = 10**deg - 1
        lo %= mod
        hi %= mod
        sum_deg = (lo+hi)*(hi-lo+1)//2
        ans += sum_deg * deg
        ans %= mod
    # 999...999+1～nについては、k+1文字が(n-10**k+1)回出てくる
    lo = 10**k
    hi = n
    lo %= mod
    hi %= mod
    sum_deg = (lo+hi)*(hi-lo+1)//2
    ans += sum_deg * (k+1)
    ans %= mod
    return ans


def main():
    le, ri = map(int, input().split())
    ri_ans = calc(ri)
    le_ans = calc(le-1)
    # print(ri_ans, le_ans)
    ans = ri_ans - le_ans
    ans %= mod
    print(ans)


main()
