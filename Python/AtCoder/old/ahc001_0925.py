import random
import time
from collections import deque
random.seed(123)


def main():
    n = int(input())
    item_list = []
    area_list = []
    # set_first
    for _ in range(n):
        x, y, r = map(int, input().split())
        area_list.append([x, y, x+1, y+1, (x, y), r])

    def check():
        if (0 <= cur_area[0] <= cur_area[2] <= 9999
            and 0 <= cur_area[1] <= cur_area[3] <= 9999
            and cur_area[0] <= cur_area[4][0] < cur_area[2]
            and cur_area[1] <= cur_area[4][1] < cur_area[3]):
            is_in_area = True
        else:
            is_in_area = False
        if not is_in_area:
            return False
        for i, area in enumerate(area_list):
            if i == cur_ind:
                continue
            x0 = max(area[0], cur_area[0])
            y0 = max(area[1], cur_area[1])
            x1 = min(area[2], cur_area[2])
            y1 = min(area[3], cur_area[3])
            if x0 <= x1 and y0 <= y1:
                return False
        return True

    st_time = time.perf_counter()
    time_limit = 4.5

    def calc_score():
        size = (cur_area[2] - cur_area[0]) * (cur_area[3] - cur_area[1])
        r = cur_area[5]
        cur_p = 1-(1-min(r, size)/max(r, size))**2
        return cur_p

    # 適当に貪欲法で埋める
    # 2分探索で、他と重ならない最大の正方形を求める
    for cur_ind, cur_area in enumerate(area_list):
        ok = 1
        ng = 10001
        r = cur_area[5]
        while ng - ok > 1:
            mid = (ok + ng) // 2
            cur_area[2] = cur_area[0] + mid
            cur_area[3] = cur_area[1] + mid
            if mid**2 <= r and check():
                ok = mid
            else:
                ng = mid
        cur_area[2] = cur_area[0] + ok
        cur_area[3] = cur_area[1] + ok

    # scoreが小さい順に、縦横に最大まで拡大
    for i in range(4):
        que = []
        for cur_ind, cur_area in enumerate(area_list):
            size = (cur_area[2] - cur_area[0]) * (cur_area[3] - cur_area[1])
            r = cur_area[5]
            # 後どれだけ追加できるかを、scoreと定義する
            cur_p = 1-(1-min(r, size)/max(r, size))**2
            score = 1-cur_p
            que.append([score, cur_ind])
        que.sort()
        for score, cur_ind in que:
            cur_area = area_list[cur_ind]
            ok = 0
            ng = 10001
            if i == 0:
                # 左に拡大
                bef1 = cur_area[0]
                while ng - ok > 1:
                    mid = (ok + ng) // 2
                    cur_area[0] = bef1 - mid
                    size = (cur_area[2] - cur_area[0]) * (cur_area[3] - cur_area[1])
                    if size <= r and check():
                        ok = mid
                    else:
                        ng = mid
                cur_area[0] = bef1 - ok
            elif i == 1:
                # 右に拡大
                bef2 = cur_area[2]
                while ng - ok > 1:
                    mid = (ok + ng) // 2
                    cur_area[2] = bef2 + mid
                    size = (cur_area[2] - cur_area[0]) * (cur_area[3] - cur_area[1])
                    if size <= r and check():
                        ok = mid
                    else:
                        ng = mid
                cur_area[2] = bef2 + ok
            elif i == 2:
                # 上に拡大
                bef1 = cur_area[1]
                while ng - ok > 1:
                    mid = (ok + ng) // 2
                    cur_area[1] = bef1 - mid
                    size = (cur_area[2] - cur_area[0]) * (cur_area[3] - cur_area[1])
                    if size <= r and check():
                        ok = mid
                    else:
                        ng = mid
                cur_area[1] = bef1 - ok
            else:
                bef2 = cur_area[3]
                while ng - ok > 1:
                    mid = (ok + ng) // 2
                    cur_area[3] = bef2 + mid
                    size = (cur_area[2] - cur_area[0]) * (cur_area[3] - cur_area[1])
                    if size <= r and check():
                        ok = mid
                    else:
                        ng = mid
                cur_area[3] = bef2 + ok

    # 山登り法
    heat = 100
    while time.perf_counter() - st_time <= time_limit:
        cur_ind = random.randint(0, n-1)
        cur_area = area_list[cur_ind]
        ori = random.randint(0, 8)
        if ori >= 4:
            ori = random.randint(0, 8)
        is_cold = (random.randint(0, 100) <= 50)
        cur_score = calc_score()
        if is_cold:
            heat *= -1
        if ori == 0:
            cur_area[0] -= heat
        elif ori == 1:
            cur_area[1] -= heat
        elif ori == 2:
            cur_area[2] += heat
        elif ori == 3:
            cur_area[3] += heat
        elif ori == 4:
            cur_area[0] -= heat//2
            cur_area[2] -= heat//2
        elif ori == 5:
            cur_area[0] += heat//2
            cur_area[2] += heat//2
        elif ori == 6:
            cur_area[1] -= heat//2
            cur_area[3] -= heat//2
        elif ori == 7:
            cur_area[1] += heat//2
            cur_area[3] += heat//2

        aft_score = calc_score()
        is_ok = (aft_score >= cur_score) or random.randint(0, 100) <= heat*0.7

        if not (check() and is_ok):
            if ori == 0:
                cur_area[0] += heat
            elif ori == 1:
                cur_area[1] += heat
            elif ori == 2:
                cur_area[2] -= heat
            elif ori == 3:
                cur_area[3] -= heat
            elif ori == 4:
                cur_area[0] += heat//2
                cur_area[2] += heat//2
            elif ori == 5:
                cur_area[0] -= heat//2
                cur_area[2] -= heat//2
            elif ori == 6:
                cur_area[1] += heat//2
                cur_area[3] += heat//2
            elif ori == 7:
                cur_area[1] -= heat//2
                cur_area[3] -= heat//2
        if is_cold:
            heat *= -1
        if random.randint(0, 1000) == 0:
            heat = max(heat-1, 1)
    # 出力
    
    for a, b, c, d, *_ in area_list:
        print(a, b, c, d)


main()
