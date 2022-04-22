from collections import Counter
import sys
sys.setrecursionlimit(10**6)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# O(300**3)まで
def main():
    p_end, k = map(int, input().split())
    p_list = [tuple(map(int, input().split())) for _ in range(p_end)]

    # 1点にk個以上集まっている場合は、例外
    same_cnt_of = Counter(p_list)
    if max(same_cnt_of.values()) >= k:
        print('Infinity')
        return

    ans_set = set()

    for fr_i in range(p_end):
        fr = p_list[fr_i]
        # 原点にスライド移動させる
        new_p_list = [(p[0]-fr[0], p[1]-fr[1]) for p in p_list]
        """
        for to_i in range(fr_i+1, p_end):
            to = new_p_list[to_i]
            # frからtoにかけての直線を数える
        """
        # new_p_listを最小公倍数を取って円上の代表元化する。
        circle_p_list = []
        for i in range(p_end):
            p = list(new_p_list[i])
            if p[1] < 0:
                p[0], p[1] = -p[0], -p[1]
            if p[1] == 0 and p[0] < 0:
                p[0] = -p[0]
            if p == [0, 0]:  # frと重複しているやつは別途処理
                continue
            gcd_ = gcd(p[0], p[1])
            p[0] //= gcd_
            p[1] //= gcd_
            circle_p_list.append(tuple(p))
        cnt_of = Counter(circle_p_list)
        # k個以上ある円上の代表元の数が答えの候補
        for key, value in cnt_of.items():
            if value + same_cnt_of[fr] >= k:
                dx, dy = key
                # keyと、frから、切片を求める
                # fr_y - fr_x/dx * dy
                # (dx*fr_y - dy*fr_x) / dx
                fr_x, fr_y = fr
                if dx == 0:  # y軸と平行な時は、fr_xのみが重要
                    ans_set.add((dx, dy, fr_x, 0))
                    continue
                elif dy == 0:
                    ans_set.add((dx, dy, 0, fr_y))
                    continue
                up = dx*fr_y - dy*fr_x
                down = dx
                if up < 0:
                    up, down = -up, -down
                if up == 0 and down < 0:
                    down = -down
                gcd_ = gcd(up, down)
                up //= gcd_
                down //= gcd_
                ans_set.add((dx, dy, up, down))

    print(len(ans_set))


main()
