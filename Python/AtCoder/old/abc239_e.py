import sys
sys.setrecursionlimit(10**6)


# クエリ先読み?
# kは小さい
# 各頂点別に、その部分木の値を大きい順に保持する
# サイズは、20までとする
def main():
    node_end, query_end = map(int, input().split())
    X = list(map(int, input().split()))
    nei_of = [[] for _ in range(node_end)]
    for _ in range(node_end-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    query_list = []
    for _ in range(query_end):
        v, k = map(int, input().split())
        v -= 1
        k -= 1
        query_list.append((v, k))

    # 部分木の持つ整数のうち、大きい順のリスト
    # ただしサイズは20まで
    values_of = [[] for _ in range(node_end)]
    values_end = 21

    def dfs(cur, pre):
        cur_values = values_of[cur]
        cur_values.append(X[cur])
        for nex in nei_of[cur]:
            if nex == pre:
                continue
            dfs(nex, cur)
            nex_values = values_of[nex]
            for val in nex_values:
                cur_values.append(val)
            cur_values.sort(reverse=True)
            while len(cur_values) >= values_end:
                cur_values.pop()

    dfs(0, -1)

    for v, k in query_list:
        print(values_of[v][k])


main()
