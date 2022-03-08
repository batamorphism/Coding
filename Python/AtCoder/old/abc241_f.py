from collections import defaultdict, deque


def main():
    r_end, c_end, n = map(int, input().split())
    st_r, st_c = map(lambda x: int(x)-1, input().split())
    en_r, en_c = map(lambda x: int(x)-1, input().split())
    rc_list = []
    for _ in range(n):
        r, c = map(lambda x: int(x)-1, input().split())
        rc_list.append((r, c))
    INF = float('inf')

    # 各行ごとに持っている石のリストと
    # 各列ごとに持っている石のリストを作る
    # stones_of_col[col]で、col列目に石がどこにあるか
    stones_of_col = defaultdict(lambda: [-INF, INF])
    stones_of_row = defaultdict(lambda: [-INF, INF])
    for r, c in rc_list:
        stones_of_row[r].append(c)
        stones_of_col[c].append(r)

    # bisect用にソート
    for stones in stones_of_col.values():
        stones.sort()
    for stones in stones_of_row.values():
        stones.sort()

    def bisect_left(array, val):
        # arrayに含まれる、val以下の数値の最大値を求める
        ok = -1
        ng = len(array)
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if array[mid] <= val:
                ok = mid
            else:
                ng = mid
        return array[ok]

    def bisect_right(array, val):
        # arrayに含まれる、val以上の数値の最小値を求める
        ok = len(array)
        ng = -1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if array[mid] >= val:
                ok = mid
            else:
                ng = mid
        return array[ok]

    def nei_of(pre_r, pre_c):
        # pre_r, pre_cから石にぶつかるまで移動したときの移動先
        # 右に移動
        stone = bisect_right(stones_of_row[pre_r], pre_c)
        if stone != INF and stone != -INF:
            cur_r = pre_r
            cur_c = stone - 1
            yield cur_r, cur_c
        # 左に移動
        stone = bisect_left(stones_of_row[pre_r], pre_c)
        if stone != INF and stone != -INF:
            cur_r = pre_r
            cur_c = stone + 1
            yield cur_r, cur_c
        # 下に移動
        stone = bisect_right(stones_of_col[pre_c], pre_r)
        if stone != INF and stone != -INF:
            cur_c = pre_c
            cur_r = stone - 1
            yield cur_r, cur_c
        # 上に移動
        stone = bisect_left(stones_of_col[pre_c], pre_r)
        if stone != INF and stone != -INF:
            cur_c = pre_c
            cur_r = stone + 1
            yield cur_r, cur_c

    # bfs
    que = deque([(st_r, st_c)])
    dist = defaultdict(lambda: INF)
    dist[(st_r, st_c)] = 0

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
