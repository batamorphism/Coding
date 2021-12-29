# https://atcoder.jp/contests/typical90/submissions/26995086
import sys
sys.setrecursionlimit(10**6)


def main():
    n, m = map(int, input().split())
    pos_nei_of = [[] for _ in range(n)]
    neg_nei_of = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        pos_nei_of[a].append(b)
        neg_nei_of[b].append(a)

    # SCC 強連結成分分解
    pos_color = ['w']*n
    neg_color = ['w']*n
    pos_data = []
    neg_data = []

    def dfs(pre, color, nei_of, data):
        ret = 1
        for cur in nei_of[pre]:
            if color[cur] == 'w':
                color[cur] = 'g'
                ret += dfs(cur, color, nei_of, data)
        data.append(pre)  # 帰りがけにデータを追加
        return ret  # 探索したnode数を返す

    # first DFS
    for node in range(n):
        if pos_color[node] == 'w':
            pos_color[node] = 'g'
            dfs(node, pos_color, pos_nei_of, pos_data)

    # second DFS
    # 各CSSの個数の組み合わせ数は、cnt*(cnt-1)//2であり、それの総和が答え
    ans = 0
    for node in reversed(pos_data):
        if neg_color[node] == 'w':
            neg_color[node] = 'g'
            cnt = dfs(node, neg_color, neg_nei_of, neg_data)
            for node in neg_data:
                pass  # 各nodeは同じ連結成分に属する
            neg_data.clear()
            ans += cnt*(cnt-1)//2

    print(ans)


main()

