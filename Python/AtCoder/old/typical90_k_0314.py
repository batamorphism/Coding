# 締め切りが近い順に貪欲
def main():
    n = int(input())
    day_end = 5001
    job_list = [tuple(map(int, input().split())) for _ in range(n)]
    job_list.sort(key=lambda x: x[0])

    # DP[cur_job][work_day] := work_day日既に働いた状態での、報酬の最大値
    # 配るDP
    DP = [0]*day_end
    for job in job_list:
        new_DP = [0]*day_end
        d_i, c_i, s_i = job
        for bef_work_day in range(day_end):
            # 1. このjobでは働かない
            new_DP[bef_work_day] = max(new_DP[bef_work_day], DP[bef_work_day])
            # 2. このjobで働く
            aft_work_day = bef_work_day + c_i
            if aft_work_day > d_i:  # 働くことはできない
                continue
            new_DP[aft_work_day] = max(new_DP[aft_work_day], DP[bef_work_day]+s_i)
        DP = new_DP[:]
    ans = max(DP)
    print(ans)


main()
