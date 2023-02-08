import bisect
from collections import defaultdict, deque
INF = float('inf')


def main():
    r_end, c_end, n = map(int, input().split())
    st_r, st_c = map(lambda x: int(x)-1, input().split())
    en_r, en_c = map(lambda x: int(x)-1, input().split())

    stone_of_r = defaultdict(lambda: [-INF, INF])
    stone_of_c = defaultdict(lambda: [-INF, INF])
    for _ in range(n):
        r, c = map(lambda x: int(x)-1, input().split())
        stone_of_r[r].append(c)
        stone_of_c[c].append(r)

    for arr in stone_of_r.values():
        arr.sort()
    for arr in stone_of_c.values():
        arr.sort()

    def nei_of(pre_r, pre_c):
        lo_stone_ind = bisect.bisect_left(stone_of_r[pre_r], pre_c)-1
        hi_stone_ind = lo_stone_ind+1

        cur_c = stone_of_r[pre_r][lo_stone_ind]+1
        cur_r = pre_r
        if cur_c not in [INF, -INF]:
            yield cur_r, cur_c

        cur_c = stone_of_r[pre_r][hi_stone_ind]-1
        cur_r = pre_r
        if cur_c not in [INF, -INF]:
            yield cur_r, cur_c

        lo_stone_ind = bisect.bisect_left(stone_of_c[pre_c], pre_r)-1
        hi_stone_ind = lo_stone_ind+1
        cur_r = stone_of_c[pre_c][lo_stone_ind]+1
        cur_c = pre_c
        if cur_r not in [INF, -INF]:
            yield cur_r, cur_c

        cur_r = stone_of_c[pre_c][hi_stone_ind]-1
        if cur_r not in [INF, -INF]:
            yield cur_r, cur_c

    que = deque()
    dist = defaultdict(lambda: INF)
    dist[(st_r, st_c)] = 0
    que.append((st_r, st_c))
    while que:
        pre_r, pre_c = que.popleft()
        pre_d = dist[(pre_r, pre_c)]
        cur_d = pre_d + 1
        for cur_r, cur_c in nei_of(pre_r, pre_c):
            if dist[(cur_r, cur_c)] <= cur_d:
                continue
            dist[(cur_r, cur_c)] = cur_d
            que.append((cur_r, cur_c))

    ans = dist[(en_r, en_c)]
    if ans == INF:
        ans = -1
    print(ans)


main()
