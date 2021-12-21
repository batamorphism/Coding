import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)


# 2分木
def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    # -1:未定義、0:黒、1:白
    col_of = [-1] * n
    col_of[0] = 0

    """
    def dfs(pre):
        pre_col = col_of[pre]
        cur_col = 1 ^ pre_col
        for cur in nei_of[pre]:
            if col_of[cur] == -1:
                # preの色を反転させて着色
                col_of[cur] = cur_col
                dfs(cur)
    """
    que = deque()
    que.append(0)
    while que:
        pre = que.popleft()
        pre_col = col_of[pre]
        cur_col = 1 ^ pre_col
        for cur in nei_of[pre]:
            if col_of[cur] == -1:
                col_of[cur] = cur_col
                que.appendleft(cur)

    col0_cnt = col_of.count(0)
    col1_cnt = col_of.count(1)
    if col0_cnt > col1_cnt:
        target_col = 0
    else:
        target_col = 1
    ans = []
    for node in range(n):
        if col_of[node] == target_col:
            ans.append(node + 1)
            if len(ans) == n // 2:
                break

    print(*ans)


main()
