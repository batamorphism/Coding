def main():
    n, c = map(int, input().split())
    A = [int(input()) for _ in range(n)]
    cnt_odd_dic = {}
    cnt_eve_dic = {}
    for i, a in enumerate(A):
        if i % 2 == 0:
            cnt_eve_dic[a] = cnt_eve_dic.get(a, 0)+1
        else:
            cnt_odd_dic[a] = cnt_odd_dic.get(a, 0)+1
    cnt_odd = [(val, key) for key, val in cnt_odd_dic.items()]
    cnt_eve = [(val, key) for key, val in cnt_eve_dic.items()]
    cnt_odd.sort(reverse=True)
    cnt_eve.sort(reverse=True)

    # 最も多い色は何か
    frec_cnt_odd, frec_col_odd = cnt_odd[0]
    frec_cnt_eve, frec_col_eve = cnt_eve[0]

    if frec_col_odd == frec_col_eve:
        if len(cnt_eve) >= 2:
            frec_cnt_eve, frec_col_eve = cnt_eve[1]
        else:
            frec_cnt_eve, frec_col_eve = 0, 0
        change_num1 = n-frec_cnt_odd-frec_cnt_eve

        frec_cnt_eve, frec_col_eve = cnt_eve[0]
        if len(cnt_odd) >= 2:
            frec_cnt_odd, frec_col_odd = cnt_odd[1]
        else:
            frec_cnt_odd, frec_col_odd = 0, 0
        change_num2 = n-frec_cnt_odd-frec_cnt_eve

        change_num = min(change_num1, change_num2)
    else:
        change_num = n-frec_cnt_odd-frec_cnt_eve

    print(change_num*c)


main()
