# 桁DP
def main():
    num = int(input())
    k = int(input())

    num_list = list(map(int, str(num)))
    DP = [0]*(k+1)
    top_k = 0

    for i, n_i in enumerate(num_list):
        new_DP = [0]*(k+1)

        # 1. 前の数字の末尾に0～9を追加
        if i != 0:
            for pre_k in range(k+1):
                # 0を追加
                new_DP[pre_k] += DP[pre_k]
                # 1~9を追加
                cur_k = pre_k + 1
                if cur_k <= k:
                    new_DP[cur_k] += DP[pre_k]*9

        # 2. 1桁の整数を追加
        if i != 0:
            new_DP[1] += 9

        # 3. top_kから派生
        if i == 0:
            val_begin = 1
        else:
            val_begin = 0
        val_end = n_i
        for val in range(val_begin, val_end):
            if val == 0:
                cur_k = top_k
            else:
                cur_k = top_k + 1
            if cur_k <= k:
                new_DP[cur_k] += 1

        # 4. 更新処理
        if n_i != 0:
            top_k += 1
        for k in range(k+1):
            DP[k] = new_DP[k]

    # 5. top_kそのものの処理
    if top_k <= k:
        DP[top_k] += 1

    ans = DP[-1]
    print(ans)


main()
