# greedy
# 座標xで爆弾を使うと
# [x, x+2*D]の範囲の体力をA減らすことができる
import heapq
from collections import deque


def main():
    n, d, a = map(int, input().split())
    bomb_pos = deque()
    cur_damage = 0

    monster_list = [tuple(map(int, input().split())) for _ in range(n)]
    monster_list.sort()

    ans = 0
    for x, h in monster_list:
        # x が [bomb_pos, bomb_pos+2*d] の範囲に入っていない場合、
        # bomb_posをpopし、cur_damageを更新する
        while bomb_pos and not (bomb_pos[0][0] <= x <= bomb_pos[0][0] + 2*d):
            rm_pos, rm_cnt = bomb_pos.popleft()
            cur_damage -= a*rm_cnt
        cur_h = h - cur_damage
        if cur_h <= 0:
            continue
        cur_cnt = (cur_h + a - 1)//a  # 切り上げ
        cur_damage += cur_cnt*a
        bomb_pos.append((x, cur_cnt))
        ans += cur_cnt

    print(ans)


main()
