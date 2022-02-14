from collections import defaultdict


# 貰うDP
def main():
    MOD = 10000
    n, k = map(int, input().split())
    rule_list = [tuple(map(int, input().split())) for _ in range(k)]

    rule_of = defaultdict(lambda: -1)
    for rule in rule_list:
        day, num = rule
        rule_of[day] = num

    # DP[day][cur][pre]
    DP = [[[0]*4 for _ in range(4)] for _ in range(n+1)]
    DP[0][0][0] = 1

    for day in range(1, n+1):
        if rule_of[day] == -1:
            cur_begin = 1
            cur_end = 4
        else:
            cur_begin = rule_of[day]
            cur_end = cur_begin + 1
        for cur in range(cur_begin, cur_end):
            if day == 1:
                pre_begin = 0
                pre_end = 1
            else:
                pre_begin = 1
                pre_end = 4
            for pre in range(pre_begin, pre_end):
                if day <= 2:
                    pre2_begin = 0
                    pre2_end = 1
                else:
                    pre2_begin = 1
                    pre2_end = 4
                for pre2 in range(pre2_begin, pre2_end):
                    if cur == pre == pre2:
                        continue
                    DP[day][cur][pre] += DP[day-1][pre][pre2]
                    DP[day][cur][pre] %= MOD

    ans = 0
    for cur in range(1, 4):
        for pre in range(1, 4):
            ans += DP[n][cur][pre]
            ans %= MOD

    print(ans)


main()
