from collections import namedtuple
import sys

Config = namedtuple('Config', ['node_end', 'nei_of', 'color'])
sys.setrecursionlimit(10**9)


def main():
    node_end = int(input())
    edge_list = []
    for _ in range(node_end-1):
        a, b = map(int, input().split())
        edge_list.append((a-1, b-1))
    nei_of = [[] for _ in range(node_end)]
    for edge in edge_list:
        nei_of[edge[0]].append(edge[1])
        nei_of[edge[1]].append(edge[0])

    # sort nei
    for nei in nei_of:
        nei.sort()

    start_node = 0
    color = ['w']*node_end
    cfg = Config(node_end, nei_of, color)
    dfs(start_node, cfg)


def dfs(pre_node: int, cfg: Config):
    print(pre_node+1)
    cfg.color[pre_node] = 'g'
    for cur_node in cfg.nei_of[pre_node]:
        if cfg.color[cur_node] == 'w':
            dfs(cur_node, cfg)
            print(pre_node+1)
    cfg.color[pre_node] = 'b'


main()
