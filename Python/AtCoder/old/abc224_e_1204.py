# 数字が大きい順に処理する
# 各r, cに対し、最大の処理回数を求めておく
# 最大の処理回数+1が、r, cの最大の処理回数を上書きする
def main():
    r_end, c_end, n = map(int, input().split())
    query_list = []
    for i in range(n):
        r, c, a = map(int, input().split())
        r -= 1
        c -= 1
        query_list.append((a, r, c, i))
    query_list.sort(reverse=True)

    # 各r, cについてそれぞれ最大値を求める
    ans_list = [0] * n
    max_r_of = [0] * (r_end + 1)
    max_c_of = [0] * (c_end + 1)
    batch = []
    pre_a = -1
    for a, r, c, i in query_list:
        if a != pre_a:
            # aが替わったので、batchを処理する
            for rr, cc, val in batch:
                max_r_of[rr] = max(val, max_r_of[rr])
                max_c_of[cc] = max(val, max_c_of[cc])
            batch = []
        ans = max(max_r_of[r], max_c_of[c])
        batch.append((r, c, ans+1))
        ans_list[i] = ans
        pre_a = a

    print(*ans_list, sep='\n')


main()
