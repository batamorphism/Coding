def main():
    n, p = map(int, input().split())
    # DP[今まで取り除いた辺の数] = 組み合わせ数
    DP = [0] * (n+1)
    DP2 = [0] * (n+1)  # 連結ではないが、次をつなげば連結になるやつ
    DP[0] = 1  # 初手は、辺が一個しかない
    DP2[1] = 1  # 離れてるタイプ
    for i in range(1, n):
        new_DP = [0] * (n+1)
        new_DP2 = [0] * (n+1)
        # 今、既にi個の頂点が存在している
        # 1. 今まで連結だったものに追加
        for pre_cnt in range(n+1):
            new_DP[pre_cnt] += DP[pre_cnt]  # 全て足す
            cur_cnt = pre_cnt + 1
            if cur_cnt <= n:
                new_DP[cur_cnt] += DP[pre_cnt] * 3
        # 2. 今まで非連結だったもの
        for cnt in range(n+1):
            new_DP[cnt] += DP2[cnt]  # 非連結の個数は変わらない
        for pre_cnt in range(n+1):
            # | | を追加
            cur_cnt = pre_cnt + 1
            if cur_cnt <= n:
                new_DP2[cur_cnt] += DP2[pre_cnt]
            # 連結だったものに、. |か| . を追加
            cur_cnt = pre_cnt + 2
            if cur_cnt <= n:
                new_DP2[cur_cnt] += DP[pre_cnt]*2

        for cnt in range(n+1):
            DP[cnt] = new_DP[cnt] % p
            DP2[cnt] = new_DP2[cnt] % p

    print(*DP[1:n])


main()
