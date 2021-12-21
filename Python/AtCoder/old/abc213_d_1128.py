import sys
sys.setrecursionlimit(10**6)


# オイラーツアー
def main():
    node_end = int(input())
    nei_of = [[] for _ in range(node_end)]

    for _ in range(node_end - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    for nei in nei_of:
        nei.sort()

    ans = []
    col = ['w']*node_end

    def dfs(pre):
        for cur in nei_of[pre]:
            if col[cur] == 'w':
                col[cur] = 'b'
                # 行きがけに追加
                ans.append(cur + 1)
                dfs(cur)
                # 帰りがけに追加
                ans.append(pre + 1)

    col[0] = 'b'
    ans.append(1)
    dfs(0)

    print(*ans)


main()
