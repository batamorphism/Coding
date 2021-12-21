# A,Bそれぞれすべての組み合わせを試すことはできない
# AとBを結合して、N+M長さのリストに対し
# まずソートした後
# それぞれのリストには、数値と元がAだったかBだったかをくっつけておいて
# aからb、もしくはbからaに変わった時の差の絶対値の最小値を調べる
# これはO(N+M)

def main():
    n, m, *_AB = map(int, open(0).read().split())
    A = [[_AB[i], 'a'] for i in range(n)]
    B = [[_AB[n+i], 'b'] for i in range(m)]
    AB = A+B
    AB.sort()

    ans = 1e10
    pre_num = 1e10
    pre_ab = 'a'
    for v in AB:
        if pre_ab != v[1]:  # aからbとかに変わったぜ
            hoge = abs(pre_num-v[0])
            if hoge < ans:  # 差の絶対値がもっとちっさいパターンが見つかったぜ
                ans = hoge
        pre_num = v[0]
        pre_ab = v[1]

    print(ans)


main()
