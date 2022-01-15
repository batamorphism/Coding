# 締め切りが近い順に見る
# i番目の仕事を見た状態で、今までx日仕事している状態における、報酬の最大値をDP[i][x]とする
# (i, x) <- (i-1, x)  i番目の仕事をしない場合
# (i, x) <- (i-1, x-c_i)  i番目の仕事をする場合。d_i >= xが必要
def main():
    n = int(input())
    job_list = [(-1, -1, -1)]
    for _ in range(n):
        d, c, s = map(int, input().split())
        job_list.append((d, c, s))

    job_list.sort(key=lambda x: x[0])

    x_end = 5001

    DP = [[0]*x_end for _ in range(n+1)]

    for i in range(1, n+1):
        d_i, c_i, s_i = job_list[i]
        for x in range(x_end):
            dp = DP[i-1][x]  # i番目の仕事をしない場合
            if d_i >= x and x-c_i >= 0:
                dp = max(dp, DP[i-1][x-c_i] + s_i)  # i番目の仕事をする場合
            DP[i][x] = dp

    print(max(DP[n]))


main()
