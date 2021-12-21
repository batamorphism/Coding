from collections import deque
from collections import namedtuple

Node = namedtuple('Node', ['r', 'c'])
Config = namedtuple('Config', ['h', 'w', 'town'])


def main():
    INF = 10**10
    h, w = map(int, map(int, input().split()))
    town = []
    for _ in range(h):
        town.append(input())
    config = Config(h, w, town)
    # 01BFS
    dist = [[INF]*w for _ in range(h)]
    que = deque()
    start_node = Node(r=0, c=0)
    dist[0][0] = 0
    que.appendleft(start_node)
    while que:
        pre_node = que.popleft()
        if pre_node.r == h-1 and pre_node.c == w-1:
            break
        # COST 0
        neighbor = cost0_neighbor_of(pre_node, config)
        for cur_node in neighbor:
            if dist[cur_node.r][cur_node.c] <= dist[pre_node.r][pre_node.c]:
                continue
            dist[cur_node.r][cur_node.c] = dist[pre_node.r][pre_node.c]
            que.appendleft(cur_node)

        # COST1
        neighbor = cost1_neighbor_of(pre_node, config)
        for cur_node in neighbor:
            if dist[cur_node.r][cur_node.c] <= dist[pre_node.r][pre_node.c]+1:
                continue
            dist[cur_node.r][cur_node.c] = dist[pre_node.r][pre_node.c]+1
            que.append(cur_node)

    print(dist[-1][-1])


def cost0_neighbor_of(node: Node, config: Config) -> list:
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ret = []
    for i in range(4):
        cur_r = node.r+dr[i]
        cur_c = node.c+dc[i]
        if cur_r < 0 or cur_r >= config.h or cur_c < 0 or cur_c >= config.w:
            continue
        if config.town[cur_r][cur_c] == '#':
            continue
        ret.append(Node(r=cur_r, c=cur_c))
    return ret


def cost1_neighbor_of(node: Node, config: Config) -> list:
    """
    X###X
    #####
    ##@##
    #####
    X###X
    """
    dr_list = [-2, -1, 0, 1, 2]
    dc_list = [-2, -1, 0, 1, 2]
    ret = []
    for dr in dr_list:
        for dc in dc_list:
            if abs(dr) == 2 and abs(dc) == 2:
                continue
            if dr==0 and dc == 0:
                continue
            cur_r = node.r+dr
            cur_c = node.c+dc
            if cur_r < 0 or cur_r >= config.h or cur_c < 0 or cur_c >= config.w:
                continue
            ret.append(Node(r=cur_r, c=cur_c))
    return ret


main()
