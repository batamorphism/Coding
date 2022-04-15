from collections import deque


# BFS?
# ノード数は2,250,000 10**6オーダー
def main():
    rc_end = int(input())
    st_r, st_c = map(int, input().split())
    st_r -= 1
    st_c -= 1
    en_r, en_c = map(int, input().split())
    en_r -= 1
    en_c -= 1
    grid = [input() for _ in range(rc_end)]

    def in_grid(r, c):
        return 0 <= r < rc_end and 0 <= c < rc_end

    que = deque()
    que.append((st_r, st_c))
    INF = float('inf')
    dist = [[INF]*rc_end for _ in range(rc_end)]
    dist[st_r][st_c] = 0

    def nei_of(pre_r, pre_c, pre_d):
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            cur_r, cur_c = pre_r, pre_c
            while True:
                cur_r += dr
                cur_c += dc
                if not (in_grid(cur_r, cur_c) and grid[cur_r][cur_c] != '#'):
                    break
                if dist[cur_r][cur_c] <= pre_d:
                    # 既にそこに到達している場合は、打ち切ってよい
                    break
                yield cur_r, cur_c

    while que:
        pre_r, pre_c = que.popleft()
        pre_d = dist[pre_r][pre_c]
        cur_d = pre_d + 1
        for cur_r, cur_c in nei_of(pre_r, pre_c, pre_d):
            if dist[cur_r][cur_c] > cur_d:
                dist[cur_r][cur_c] = cur_d
                que.append((cur_r, cur_c))

    ans = dist[en_r][en_c]
    if ans == INF:
        ans = -1
    print(ans)


main()
