from collections import Counter


def main():
    n = int(input())
    # D_cnt = [0]*d_end
    D = [0] + list(map(int, input().split()))
    D_cnt = Counter(D)

    INF = float('inf')
    ans = -INF

    # 0時、12時は1通り->2人以上いたら0
    # それ以外は2通り->3人以上いたら0

    # check
    if D_cnt[0] >= 2:
        print(0)
        return
    elif D_cnt[12] >= 2:
        print(0)
        return
    for i in range(1, 12):
        if D_cnt[i] >= 3:
            print(0)
            return

    # 各時間帯について、2時か22時どっちに配置するか、
    # t or 24-t
    # 1, ..., 11の11通りについてbit全探索
    ALL = 1 << 11
    for bit in range(ALL):
        is_upper = [False]*13
        for i in range(11):
            if (bit >> i) & 1:
                is_upper[i+1] = True

        t_list = []
        for i in range(13):
            if D_cnt[i] == 1:
                if is_upper[i]:
                    t_list.append(24-i)
                else:
                    t_list.append(i)
            elif D_cnt[i] == 2:
                t_list.append(24-i)
                t_list.append(i)
        # calc_s
        t_list.sort()
        t_list.append(24)
        s = INF
        for i in range(len(t_list)-1):
            s = min(s, t_list[i+1]-t_list[i])
        ans = max(ans, s)

    print(ans)


main()
