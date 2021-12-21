# 最短経路の長さを求めて
# マス目全体の数-元から#の数-最短経路-1の長さが答え
from collections import deque
INF = 10**9


def main():
    r_end, c_end = map(int, input().split())
    table = [input() for _ in range(r_end)]

    def nei_of(pre):
        r, c = pre
        Dc = [0, -1, 0, 1]
        Dr = [-1, 0, 1, 0]
        for dc, dr in zip(Dc, Dr):
            cur_r, cur_c = r + dr, c + dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if table[cur_r][cur_c] == '#':
                continue
            yield (cur_r, cur_c)

    # BFS
    dist = [[INF] * c_end for _ in range(r_end)]
    que = deque()
    dist[0][0] = 0
    que.append((0, 0))

    while que:
        pre = que.popleft()
        r, c = pre
        d = dist[r][c]
        d += 1
        for cur in nei_of(pre):
            r, c = cur
            if dist[r][c] <= d:
                continue
            dist[r][c] = d
            que.append(cur)

    d = dist[r_end-1][c_end-1]
    if d == INF:
        print(-1)
        return

    total = r_end*c_end
    cnt = 0
    for row in table:
        for s in row:
            if s == '#':
                cnt += 1
    ans = total - cnt - d - 1
    print(ans)


main()
