# 貪欲に、左端にモンスターが居たら、それを破壊する
# 与えたダメージは2*Dの範囲にいるモンスターの体力も減らす
# キューで、爆弾を使った座標と、与えたダメージを覚えておいて
# キューの総和を別途取っておく(しゃくとり法)
from collections import deque


def main():
    n, d, a = map(int, input().split())
    d *= 2
    monster_list = [tuple(map(int, input().split())) for _ in range(n)]
    monster_list.sort()

    ans = 0
    que = deque()
    sum_damage = 0
    for monster in monster_list:
        x, h = monster
        # ダメージを与えられる範囲は、
        # [x-d, x]の範囲
        while que and que[0][0] < x-d:
            rm = que.popleft()
            sum_damage -= rm[1]
        h -= sum_damage
        if h <= 0:
            continue
        use_bomb_cnt = (h+a-1) // a
        ans += use_bomb_cnt
        damage = use_bomb_cnt*a
        # print(x, use_bomb_cnt, damage)
        que.append((x, damage))
        sum_damage += damage

    print(ans)


main()
