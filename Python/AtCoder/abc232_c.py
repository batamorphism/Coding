# n <= 8
# 8! = 40320
# 全探索
from itertools import permutations


def main():
    node_end, edge_end = map(int, input().split())
    # 隣接行列が同じかどうかを確認する
    A_edge = [[0] * node_end for _ in range(node_end)]
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A_edge[a][b] = 1
        A_edge[b][a] = 1

    B_edge_list = []
    for _ in range(edge_end):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        B_edge_list.append((c, d))

    for perm in permutations(range(node_end)):
        B_edge = [[0] * node_end for _ in range(node_end)]
        # node -> perm[node]に置換する
        for c, d in B_edge_list:
            c, d = perm[c], perm[d]
            B_edge[c][d] = 1
            B_edge[d][c] = 1
        if A_edge == B_edge:
            print('Yes')
            return

    print('No')


main()
