mod = 998244353
bit_max = 3010
data = [0]*(bit_max+10)


def add(pos, val):
    pos += 1
    while pos < bit_max:
        data[pos] += val
        data[pos] %= mod
        pos += pos & -pos
    return


def getsum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += data[pos]
        ret %= mod
        pos -= pos & -pos
    return ret


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [-1]+A
    B = [-1]+B
    # DP[i][x] = 長さiで末尾xのcの組み合わせ数
    DP = [0]*(3000+1)
    DP[0] = 1
    add(0, 1)
    for i in range(1, n+1):
        for x in range(3000, -1, -1):
            if not(A[i] <= x <= B[i]):
                add(x, -DP[x])
                DP[x] = 0
                continue
            # DP[0]~DP[x]の合計をとる
            DP[x] = getsum(x)
            add(x, getsum(x-1))
    ans = getsum(bit_max-1)
    print(ans)


main()
