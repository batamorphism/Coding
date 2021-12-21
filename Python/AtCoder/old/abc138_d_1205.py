import sys
sys.setrecursionlimit(10**6)


def main():
    n, q = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    # 各nodeにいくつ足すか
    add_of = [0]*n
    for _ in range(q):
        p, x = map(int, input().split())
        p -= 1
        add_of[p] += x

    cnt = [0]*n
    color = ['w']*n

    def dfs(cur_node, pre_val):
        cur_val = pre_val+add_of[cur_node]
        cnt[cur_node] = cur_val
        for nex in nei_of[cur_node]:
            if color[nex] == 'w':
                color[nex] = 'b'
                dfs(nex, cur_val)

    color[0] = 'b'
    dfs(0, 0)

    print(*cnt)


main()
