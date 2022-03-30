from collections import defaultdict


# MOD2019上で考える
# Sを[le, ri]で見たときの整数について
# val1 * 10**dgt - val2 * 10**dgt = 0
# ゆえに、2019を法として
# val1 = val2となる組み合わせを求めればよい
# これは、左端を固定してvalを計算していって、valが重複した数を数えていけばよい
def main():
    S = list(map(int, input()))
    n = len(S)
    MOD = 2019
    # 左端を固定して、[0, ri]の一覧を取得
    que = [0]
    cur_val = 0

    for dgt, s_i in enumerate(reversed(S)):
        cur_val += pow(10, dgt, MOD) * s_i
        cur_val %= MOD
        que.append(cur_val)

    ans = 0
    cnt_of = defaultdict(int)
    for val in que:
        ans += cnt_of[val]
        cnt_of[val] += 1
    print(ans)


main()
