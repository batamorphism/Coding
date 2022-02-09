# 全探索
from collections import Counter


def main():
    n = int(input())
    D = list(map(int, input().split()))
    cnt_of = Counter(D)

    # 0時から12時までそれぞれ考える
    # 各t時に対し、tと24-t時のどちらかを採用
    # その後、時刻の差の最小値を求める
    time_end = 13
    ALL = 1 << time_end

    # あるtについて、3人以上存在する場合は、0
    for t in range(time_end):
        if cnt_of[t] >= 3:
            print(0)
            return

    INF = float('inf')
    ans = -INF
    for bit in range(ALL):
        time_list = [0, 24]
        for t in range(time_end):
            if cnt_of[t] == 2:
                time_list.append(24-t)
                time_list.append(t)
            elif cnt_of[t] == 1:
                if bit >> t & 1:
                    time_list.append(24-t)
                else:
                    time_list.append(t)
        time_list.sort()
        cur_ans = INF
        for i in range(len(time_list)-1):
            j = i + 1
            t_i = time_list[i]
            t_j = time_list[j]
            cur_ans = min(cur_ans, abs(t_j - t_i))
        ans = max(ans, cur_ans)

    print(ans)


main()
