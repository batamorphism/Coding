# 操作CとDはAとBより先にやる必要がない
# したがって、操作CDは同じ操作である
# 操作Cは、持っている宝石を1個捨てると読み替える

# 操作Aをa回
# 操作Bをb回
# 操作Cをc回
# 行うとする
# これは、Dの左からa個、右からb個選び
# 小さいほうからc個を破棄した後の総和となる
def main():
    n, k = map(int, input().split())
    V = list(map(int, input().split()))

    ans = -float('inf')
    for a in range(n+1):
        for b in range(n+1):
            if a + b > k:
                break
            if a + b > n:
                break
            for c in range(n+1):
                if a + b + c > k:
                    break
                if c > (a+b):
                    break
                AB = V[:a] + V[n-b:n]
                AB.sort()
                val = sum(AB[c:])
                ans = max(ans, val)

    if ans == -float('inf'):
        raise

    print(ans)


main()
