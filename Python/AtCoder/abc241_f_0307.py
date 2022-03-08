from collections import defaultdict, deque


def main():
    INF = float('inf')
    r_end, c_end, n = map(int, input().split())
    st_r, st_c = map(lambda x: int(x)-1, input().split())
    en_r, en_c = map(lambda x: int(x)-1, input().split())
    stone_list = []
    for _ in range(n):
        a, b = map(lambda x: int(x)-1, input().split())
        stone_list.append((a, b))

    # stone_of_row[r] := r行目にある石のリスト
    stones_of_row = defaultdict(lambda: [-INF, INF])
    stones_of_col = defaultdict(lambda: [-INF, INF])

    for r, c in stone_list:
        stones_of_row[r].append(c)
        stones_of_col[c].append(r)

    for stones in stones_of_row.values():
        stones.sort()
    for stones in stones_of_col.values():
        stones.sort()

    def in_grid(r, c):
        return 0 <= r < r_end and 0 <= c < c_end

    def nei_of(pre_r, pre_c):
        # 上下左右に移動して、石にぶつかるまで移動
        # 左に移動
        cur_r = pre_r
        stones = stones_of_row[pre_r]
        cur_c = bisect_left(stones, pre_c) + 1
        if in_grid(cur_r, cur_c):
            yield cur_r, cur_c
        # 右に移動
        cur_c = bisect_right(stones, pre_c) - 1
        if in_grid(cur_r, cur_c):
            yield cur_r, cur_c
        # 下に移動
        cur_c = pre_c
        stones = stones_of_col[pre_c]
        cur_r = bisect_right(stones, pre_r) - 1
        if in_grid(cur_r, cur_c):
            yield cur_r, cur_c
        # 上に移動
        cur_r = bisect_left(stones, pre_r) + 1
        if in_grid(cur_r, cur_c):
            yield cur_r, cur_c

    # 幅優先探索
    dist = defaultdict(lambda: INF)
    dist[(st_r, st_c)] = 0
    que = deque([(st_r, st_c)])
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


def bisect_left(arr, val):
    ok = -1
    ng = len(arr)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if arr[mid] <= val:
            ok = mid
        else:
            ng = mid
    return arr[ok]


def bisect_right(arr, val):
    ok = len(arr)
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if arr[mid] >= val:
            ok = mid
        else:
            ng = mid
    return arr[ok]


main()
