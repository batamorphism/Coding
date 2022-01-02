def main():
    n = int(input()) + 1
    D = [0] + list(map(int, input().split()))
    D.sort()
    # 円環上に配置
    cnt_of = [0] * 13
    for d in D:
        cnt_of[d] += 1

    if max(cnt_of) >= 3:
        print(0)
        return
    if cnt_of[0] >= 2:
        print(0)
        return
    if cnt_of[12] >= 2:
        print(0)
        return

    d_first = 1
    d_end = 12
    ALL = 1 << (d_end-d_first)
    INF = float('inf')
    ans = -INF
    for bit in range(ALL):
        time_list = []
        if cnt_of[0] == 1:
            time_list.append(0)
            time_list.append(24)
        if cnt_of[12] == 1:
            time_list.append(12)
        for d in range(d_first, d_end):
            if cnt_of[d] == 1:
                if bit >> (d-d_first) & 1:
                    time_list.append(d)
                else:
                    time_list.append((-d) % 24)
            elif cnt_of[d] == 2:
                time_list.append(d)
                time_list.append((-d) % 24)
        time_list.sort()
        bit_ans = INF
        for i in range(len(time_list)-1):
            bit_ans = min(bit_ans, time_list[i+1] - time_list[i])
        ans = max(ans, bit_ans)

    print(ans)


main()
