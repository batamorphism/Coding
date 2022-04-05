def main():
    while True:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            return
        solve(n, x)


def solve(n, x):
    # 1からnまでの数の中から重複なしで三つ選び、合計がxとなる組み合わせの数
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i+j >= x:
                break
            k = x-i-j
            if k <= j:
                break
            if k > n:
                continue
            # print(i, j, k)
            ans += 1
    print(ans)


main()
