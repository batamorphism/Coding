INF = 10**9


def get_cnt_of(A):
    # Aの要素数が多い順のリストを返す
    cnt_of = {}
    for a in A:
        if a != -1:
            cnt_of[a] = cnt_of.get(a, 0)+1
        else:
            cnt_of[a] = 0
    ret = []
    for key, val in cnt_of.items():
        ret.append((val, key))
    ret.sort(reverse=True)
    return ret


def main():
    # 偶数個の色をすべて同じにし、かつ
    # 奇数個の色をすべて同じにする。
    # したがって、それぞれ色の種類が最も多いものの数を取得し、全体からその数を引けばよい
    # ただし、色が同じになってしまう可能性があるので、2番目まで多い色を考えて4パターン計測する
    n, c = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    A += [-1, -1]  # 存在しない画用紙を追加
    A_odd = A[::2]
    A_eve = A[1::2]
    A_odd_cnt_of = get_cnt_of(A_odd)
    A_eve_cnt_of = get_cnt_of(A_eve)

    # 最も多い色同士
    ans = INF
    for i in range(3):
        if i == 0:
            odd_i = 0
            eve_i = 0
        elif i == 1:
            odd_i = 1
            eve_i = 0
        else:
            odd_i = 0
            eve_i = 1
        odd_cnt, odd_a = A_odd_cnt_of[odd_i]
        eve_cnt, eve_a = A_eve_cnt_of[eve_i]
        if odd_a != eve_a:
            ans = min(n-odd_cnt-eve_cnt, ans)

    print(ans*c)


main()
