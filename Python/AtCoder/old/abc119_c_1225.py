from itertools import product


def main():
    n, a, b, c = map(int, input().split())
    L = [int(input()) for _ in range(n)]

    # Lの任意の2つを足し合わせて、
    # 新たなLを作成する
    # 0, 1, 2, 3からなる長さnの数列を作り
    # 0がa, 1がb, 2がcに対応するとした場合のコストを求める
    # 組み合わせ数は4**nで間に合う
    ans = float('inf')
    for prod in product(range(4), repeat=n):
        cnt = 0
        ABCD = [0]*4
        for abcd, l_ in zip(prod, L):
            ABCD[abcd] += l_
            if abcd <= 2:
                cnt += 1
        # 結合した数は、加算した数より3少ない
        cnt -= 3
        if [x for x in ABCD[:3] if x == 0]:
            continue
        ans = min(ans, calc_cost(ABCD, cnt, a, b, c))

    print(ans)


def calc_cost(ABCD, cnt, a, b, c):
    ret = 10*cnt
    ret += abs(ABCD[0] - a)
    ret += abs(ABCD[1] - b)
    ret += abs(ABCD[2] - c)
    return ret


main()
