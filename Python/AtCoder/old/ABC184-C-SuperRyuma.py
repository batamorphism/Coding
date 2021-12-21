def main():
    # input
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    solv(r1, c1, r2, c2)


def solv(r1, c1, r2, c2):
    # かかる手数は最大でも3である
    # 1のケースは、SuperRyumaが移動できる範囲にr2, c2がある場合
    # 2のケースは、3通りルートがあり
    # 斜め移動を2回で行ける部分
    # 縦横移動を2回で行ける部分
    # 斜め移動の後縦横移動で行ける部分がある
    ans = -1
    # 0手かの確認
    if ans == -1:
        if (r1 == r2) and (c1 == c2):
            ans = 0
    # 1手で行けるかの確認
    if ans == -1:
        if (r1+c1) == (r2+c2):
            ans = 1
        elif (r1-c1) == (r2-c2):
            ans = 1
        elif abs(r1-r2) + abs(c1-c2) <= 3:
            ans = 1
    # 2手で行けるかの確認
    if ans == -1:
        if abs((r2-r1)+(c2-c1)) % 2 == 0:  # 斜め2回
            ans = 2
        elif abs(r1-r2) + abs(c1-c2) <= 6:  # 縦横2回
            ans = 2
        else:
            flag = False
            # 縦に3マス動いた先に、斜めで行ける範囲があるかを確認する
            for offset_r in range(-3, 4):  # -3～3の配列
                if (r1+c1) == (r2+offset_r+c2):
                    flag = True
                elif (r1-c1) == (r2+offset_r-c2):
                    flag = True
            if flag:
                ans = 2
    # 3手か
    if ans == -1:
        ans = 3

    print(ans)


main()
