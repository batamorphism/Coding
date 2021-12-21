# 1回の操作で、Aの要素を+-1することができる
# SUM(abs(A-B))がk以下であり、かつ差が2の倍数であればよい

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    val = 0
    for a, b in zip(A, B):
        val += abs(a - b)

    if val <= k and (val-k) % 2 == 0:
        print('Yes')
    else:
        print('No')


main()
