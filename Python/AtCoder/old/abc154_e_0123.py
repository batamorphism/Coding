def main():
    number = [0] + list(map(int, input()))
    k_max = int(input())

    # 桁DP
    high = 0
    DP = [[0]*(k_max+1) for _ in range(len(number))]
    for deg in range(len(number)-1):
        # 配るDP
        # 既に、number以下が確定している部分
        # 1. 新たに追加される1桁の数
        if deg >= 1:
            DP[deg+1][1] += 9
        # 2. 既に追加されている数の末尾に0を追加
        for k in range(k_max+1):
            DP[deg+1][k] += DP[deg][k]
        # 3. 既に追加されている数の末尾に1~9を追加
        for k in range(k_max):
            DP[deg+1][k+1] += DP[deg][k]*9
        # 4. highから生成
        # high*10 ~ high*10+number[deg]-1
        non_zero_cnt = len(str(high)) - str(high).count('0')
        nex_val = number[deg+1]
        # 4.1 0を追加
        if deg >= 1:
            if nex_val >= 1:
                k = non_zero_cnt
                if k <= k_max:
                    DP[deg+1][k] += 1
        # 4.2 1~を追加
        if nex_val >= 2:
            k = non_zero_cnt + 1
            if k <= k_max:
                DP[deg+1][k] += nex_val-1

        high *= 10
        high += nex_val
    # last value
    non_zero_cnt = len(str(high)) - str(high).count('0')
    if non_zero_cnt <= k_max:
        DP[len(number)-1][non_zero_cnt] += 1

    ans = DP[len(number)-1][k_max]
    print(ans)
    """
    for d in DP:
        print(d)
    """


main()
