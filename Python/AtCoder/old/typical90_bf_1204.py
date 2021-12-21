# ダブリング、メモ
def main():
    n, k = map(int, input().split())
    ans = calc(n, k)
    print(ans)


memo = {}
def calc(p_x, p_k):
    # xから始まる操作をk回行うときの値
    x = p_x
    k = p_k
    if (p_x, p_k) in memo:
        return memo[(p_x, p_k)]
    # print(x, k)
    if k == 1:
        # 一回だけ操作する
        y = calc_y(x)
        ret = (x+y) % 10**5
        memo[(p_x, p_k)] = ret
        return ret
    if k & 1:
        # 一回進めてkを偶数にする
        x = calc(x, 1)
        k -= 1
    x = calc(x, k // 2)
    k //= 2
    x = calc(x, k)
    memo[(p_x, p_k)] = x
    return x


def calc_y(x):
    # xの各桁の和を計算し、これをyとする
    y = 0
    x = str(x)
    for xx in map(int, x):
        y += xx
    return y


main()
