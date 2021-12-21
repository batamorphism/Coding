def main():
    n = int(input())
    S = list(input())

    # ランレングス圧縮
    rlm = []
    cnt = 1
    for pre_i in range(n):
        cur_i = pre_i + 1
        if cur_i >= n or S[cur_i] != S[pre_i]:
            rlm.append((S[pre_i], cnt))
            cnt = 1
        else:
            cnt += 1

    ALL = n*(n-1)//2
    com_cnt = 0
    for _, num in rlm:
        com_cnt += num*(num-1)//2
    print(ALL-com_cnt)


main()
