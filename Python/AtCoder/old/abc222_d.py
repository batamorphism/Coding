DATA = [[0]*3102 for _ in range(3102)]
mod = 998244353


def get_sum(len, pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += DATA[len][pos]
        ret %= mod
        pos -= pos & -pos
    return ret


def add(len, pos, x):
    pos += 1
    while pos <= 3100:
        DATA[len][pos] += x
        DATA[len][pos] %= mod
        pos += pos & -pos


def get_dp(len, x):
    # 長さlenで、末尾がx以下となる整数列Cの組み合わせ数をDATAで管理
    # return値は末尾がxとなる整数列Cの組み合わせ数とする
    return get_sum(len, x)


def add_dp(len, x, val):
    add(len, x, val)
    return 1


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # DP
    # DP[len][x] 長さlenで、末尾がxとなる整数列Cの答え
    # 上手くいかないので、dp(len, x)で管理する

    for len in range(n):
        a = A[len]
        b = B[len]
        for x in range(3010):
            if x < a or x > b:
                continue
            if len == 0:
                # val = max(min(x, b)-a+1, 0)
                val = 1
                add_dp(len, x, val)
                continue
            val = get_dp(len-1, x)
            val %= mod
            add_dp(len, x, val)

    print(get_dp(n-1, 3100) % mod)


main()
