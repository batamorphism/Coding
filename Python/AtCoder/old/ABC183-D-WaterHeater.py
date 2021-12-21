def main():
    # input
    n, w = map(int, input().split())
    S = []
    T = []
    P = []
    for _ in range(n):
        s, t, p = map(int, input().split())
        S.append(s)
        T.append(t)
        P.append(p)
    solv(n, w, S, T, P)


def solv(n: int, w: int, S: list, T: list, P: list):
    """給湯器が1つあり、毎分wリットルのお湯を供給できる
    n人の人がいて、i番目の人(0<=i<n)は時刻S[i]からT[i]まで、お湯をP[i]リットル使おうとする
    これは可能か
    n <= 2*10**5なので、O(n)で行く
    [S[i], P[i]],[T[i], -P[i]]からなるリストを考え
    ソートし
    第二要素の和がwを超える時間があるかを確認する
    Pが減る処理から先に入るので、同じ時刻に同時にSとTが入っても問題ない
    """
    STP = []
    for (s, p) in zip(S, P):
        STP.append([s, p])
    for (t, p) in zip(T, P):
        STP.append([t, -p])
    STP.sort()

    is_possible = True
    curr_w = 0
    for time, diff_w in STP:
        curr_w += diff_w
        if curr_w > w:
            is_possible = False
            break

    if is_possible:
        print('Yes')
    else:
        print('No')


main()