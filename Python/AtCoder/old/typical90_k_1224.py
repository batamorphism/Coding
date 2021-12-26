# 区間スケジューリング+DP
# 仕事iを見た段階で、今まで仕事を何日して、報酬がいくらもらえているかを管理する
# DPは1-indexed
# DP[i][work_day] = 仕事iまで考慮した段階で、work_day働いているときの報酬の最大値
# DP[i][work_day] = max(DP[i-1][work_day] <-何もしない
#                 + DP[i-1][work_day-c_i] + s_i <- 働く
# ただし、d_iまでに働けなければならないので、
# work_day <= d_iの時だけ、働く、
# work_day-c_i < 0の時は働けない

def main():
    n = int(input())
    job_list = [(0, 0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

    work_day_end = 5001
    job_end = (n+1)
    DP = [[0]*work_day_end for _ in range(job_end)]

    # 締め切りが近い順にソートする
    job_list.sort()

    for i, job in enumerate(job_list[1:], 1):
        d_i, c_i, s_i = job
        for work_day in range(work_day_end):
            dp1 = DP[i-1][work_day]
            dp2 = 0
            if work_day <= d_i and work_day-c_i >= 0:
                dp2 = DP[i-1][work_day-c_i] + s_i
            DP[i][work_day] = max(dp1, dp2)

    ans = max(DP[n])
    print(ans)


main()
