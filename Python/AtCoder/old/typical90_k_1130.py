# 区間スケジュール+DP
def main():
    n = int(input())
    day_end = 5001
    # DP[job][day] = jobまで見た状態で、合計day日作業している場合の報酬の最大値
    DP = [[0] * day_end for _ in range(n + 1)]
    job_list = [(-1, -1, -1)]
    for _ in range(n):
        dead, cost, score = map(int, input().split())
        job_list.append((dead, cost, score))

    job_list.sort()
    for i in range(1, n+1):
        dead, cost, score = job_list[i]
        for day in range(1, day_end):
            if cost <= day <= dead:
                DP[i][day] = max(DP[i-1][day], DP[i-1][day-cost] + score)
            else:
                DP[i][day] = DP[i-1][day]

    print(max(DP[n]))


main()
