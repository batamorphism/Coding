def main():
    while True:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            break
        solve(n, x)


def solve(n, x):
    # 1~nから、重複なしで3つ選び、それらの合計がxとなる組み合わせの数を求める
    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    ans += 1
    print(ans)
    return


main()
