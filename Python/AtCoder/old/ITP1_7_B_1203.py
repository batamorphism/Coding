# 全探索
def main():
    while True:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            break
        ans = 0
        # a < b < c
        for a in range(1, n + 1):
            for b in range(a+1, n + 1):
                # a+b+c=n
                if a+b >= x:
                    break
                c = x - a - b
                if c <= b:
                    continue
                if c > n:
                    continue
                # print(a, b, c)
                ans += 1
        print(ans)


main()
