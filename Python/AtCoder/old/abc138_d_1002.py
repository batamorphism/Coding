import sys
from collections import namedtuple
sys.setrecursionlimit(10**9)

Config = namedtuple('Config', ['nei_of', 'query', 'counter', 'color'])


def main():
    node_end, q = map(int, input().split())
    edge_list = []
    for _ in range(node_end-1):
        a, b = map(int, input().split())
        edge_list.append((a-1, b-1))

    # query[i] = x -> iに含まれる部分木に含まれるすべての頂点にxを足す
    query = [0]*node_end

    for _ in range(q):
        p, x = map(int, input().split())
        query[p-1] += x

    # counter[i] 操作実行後のnode:iが指す数値
    counter = [0]*node_end

    nei_of = [[] for _ in range(node_end)]
    for edge in edge_list:
        nei_of[edge[0]].append(edge[1])
        nei_of[edge[1]].append(edge[0])

    color = ['w']*node_end

    cfg = Config(nei_of, query, counter, color)
    start_node = 0
    cnt = 0
    dfs(start_node, cfg, cnt)
    print(*cfg.counter)


def dfs(pre_node, cfg: Config, cnt):
    cfg.color[pre_node] = 'g'
    cnt += cfg.query[pre_node]
    cfg.counter[pre_node] = cnt
    for cur_node in cfg.nei_of[pre_node]:
        if cfg.color[cur_node] == 'w':
            dfs(cur_node, cfg, cnt)
    cfg.color[pre_node] = 'b'


main()
