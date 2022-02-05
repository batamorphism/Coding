# 操作A, Bだけ先にやればよい
# 全探索
def main():
    n, k = map(int, input().split())
    V = list(map(int, input().split()))
    ans = -float('inf')
    for le in range(n+1):
        for ri in range(n+1):
            # 左からle個、右からri個を取り出す
            if le + ri > n:
                break
            if le + ri > k:
                break
            cur_V = V[:le] + V[n-ri:]
            cur_V.sort(reverse=True)
            can_remove = k - le - ri
            for _ in range(can_remove):
                if cur_V and cur_V[-1] < 0:
                    cur_V.pop()
            ans = max(ans, sum(cur_V))

    print(ans)


main()
