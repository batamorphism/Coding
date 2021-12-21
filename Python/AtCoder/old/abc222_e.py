# https://atcoder.jp/contests/abc222/submissions/26449528
from collections import deque
MOD = 998244353

n, m, k = map(int, input().split())
A = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, i))
    edges[v].append((u, i))

cnt = [0] * (n - 1)
for i in range(m - 1):
    s = A[i] - 1
    g = A[i + 1] - 1
    queue = deque()
    queue.append((s, -1))
    bef = [None] * n
    while queue:
        pos, bpos = queue.popleft()
        for npos, j in edges[pos]:
            if bpos == npos:
                continue
            bef[npos] = (pos, j)
            if npos == g:
                queue.clear()
                break
            queue.append((npos, pos))
    while g != s:
        g, j = bef[g]
        cnt[j] += 1

tot = sum(cnt)
if tot % 2 != k % 2 or abs(k) > tot:
    print(0)
    exit()
dp = [0] * (tot + 1)
dp[0] = 1
DP2 = [[0]*(tot+1) for _ in range(len(cnt)+1)]
DP2[0][0] = 1
for i, c in enumerate(cnt):
    for j in range((tot-k)//2, -1, -1):
        if j-c >= 0:
            dp[j] += dp[j - c]
            dp[j] %= MOD
            print("---")
            print(dp[j-c])
            print(DP2[i][j-c])
            if dp[j-c] != DP2[i][j-c]:
                print("di")
        if j-c >= 0:
            DP2[i+1][j] = DP2[i][j]+DP2[i][j-c]
        else:
            DP2[i+1][j] = DP2[i][j]
print(dp[(tot - k) // 2])
print(DP2)
