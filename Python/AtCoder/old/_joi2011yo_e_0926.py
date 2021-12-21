from collections import namedtuple
from collections import deque
Config = namedtuple('Config', ['town', 'max_r', 'max_c'])


def main():
    # input
    h, w, n = map(int, input().split())
    max_r = h-1
    max_c = w-1
    town = [input() for _ in range(max_r+1)]
    config = Config(town, max_r, max_c)

    # BFS
    INF = 10**10  # debugのためにINFを小さくした後、元に戻すのを忘れないように
    que = deque()
    # dist:power, r, c
    dist = [[[INF]*(max_c+1) for _ in range(max_r+1)] for _ in range(n+1)]
    for r in range(max_r+1):
        for c in range(max_c+1):
            if town[r][c] == 'S':
                start_node = (r, c)
    que.append(start_node)
    r, c = start_node
    dist[1][r][c] = 0
    power = 1
    cheese_set = {str(i) for i in range(1, 10)}
    while que:
        pre_node = que.popleft()  # BFSはキュー
        pre_r, pre_c = pre_node
        # power up
        if town[pre_r][pre_c] in cheese_set:
            if int(town[pre_r][pre_c]) == power:
                if power == n:
                    # eat last cheese
                    ans = dist[power][pre_r][pre_c]
                    break  # 停止処理忘れないように
                else:
                    # eat cheese
                    power += 1
                    dist[power][pre_r][pre_c] = dist[power-1][pre_r][pre_c]
                    que.clear()
        neighbor = neighbor_of(pre_node, config)
        for cur_node in neighbor:
            cur_r, cur_c = cur_node
            if dist[power][cur_r][cur_c] <= dist[power][pre_r][pre_c]+1:
                continue
            dist[power][cur_r][cur_c] = dist[power][pre_r][pre_c]+1
            que.append((cur_r, cur_c))
    print(ans)


def neighbor_of(pre_node: tuple, config: Config) -> list:
    pre_r, pre_c = pre_node
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    ret = []
    for i in range(4):
        cur_r = pre_r + dr[i]
        cur_c = pre_c + dc[i]
        if not (0 <= cur_r <= config.max_r and 0 <= cur_c <= config.max_c):
            continue
        if config.town[cur_r][cur_c] == 'X':
            continue
        ret.append((cur_r, cur_c))
    return ret


main()
