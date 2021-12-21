# 締め切りが近い順にソートする
# DP[i][x] = i番目の仕事を見た時点で、合計x日作業しているときの報酬の最大値
# DP[i][x] = max(DP[i-1][x], DP[i-1][x-cost_i] + reward_i)

def main():
    n = int(input())
    job_list= []
    for _ in range(n):
        dead, cost, reward = map(int, input().split())
        job_list.append((dead, cost, reward))

    job_list.sort()
    dead_end = 5000

    DP = [[0] * (dead_end + 1) for _ in range(n+1)]
    for i, job in enumerate(job_list, 1):
        dead_i, cost_i, reward_i = job
        for x in range(dead_end + 1):
            # この仕事をしない場合
            dp1 = DP[i-1][x]
            # この仕事をする場合
            if x <= dead_i and x-cost_i >= 0:
                dp2 = DP[i-1][x-cost_i] + reward_i
            else:
                dp2 = 0
            DP[i][x] = max(dp1, dp2)

    ans = max(DP[n])
    print(ans)


main()
