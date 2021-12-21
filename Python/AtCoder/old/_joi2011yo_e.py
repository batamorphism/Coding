from collections import deque


def main():
    # input
    h, w, n = map(int, input().split())
    town = [list(*input().split()) for _ in range(h)]

    # BFS
    que = deque()
    dist = [[[10**10]*(w) for _ in range(h)] for _ in range(n+1)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    ans = 0
    # search_start
    for r in range(h):
        for c in range(w):
            if town[r][c] == 'S':
                que.appendleft([r, c, 0])
                dist[0][r][c] = 0
    # startBFS
    while que:
        r, c, cheese = que.popleft()
        if cheese == n:
            ans = dist[cheese][r][c]
            break
        for i in range(4):
            cur_r = r+dr[i]
            cur_c = c+dc[i]
            cur_cheese = cheese
            if not(0 <= cur_r < h and 0 <= cur_c < w):
                continue
            if (town[cur_r][cur_c] == 'X'):
                continue

            # eat cheese
            if not(town[cur_r][cur_c] in ['X', '.', 'S']):
                if int(town[cur_r][cur_c]) <= cur_cheese+1:
                    cur_cheese += 1
                    town[cur_r][cur_c] = '.'  # 同じチーズを2回食べないように
                    # reset que
                    que = deque()  # BFSを仕切りなおす

            # ここの右辺の+1が重要
            if dist[cur_cheese][cur_r][cur_c] <= dist[cheese][r][c]+1:
                continue

            dist[cur_cheese][cur_r][cur_c] = dist[cheese][r][c]+1
            que.append([cur_r, cur_c, cur_cheese])

    print(ans)


main()
