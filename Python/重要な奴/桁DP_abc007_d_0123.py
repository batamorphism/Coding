# 桁DP
# 桁DPは配るDP
def main():
    a, b = map(int, input().split())
    low_ans = solve(a-1)
    high_ans = solve(b)
    # print(low_ans, high_ans)
    ans = high_ans - low_ans
    print(b - a + 1 - ans)


def solve(number_int):
    # number_int以下の値について、場合の数を求める
    if number_int == 0:
        return 1
    number_list = [0] + list(map(int, str(number_int)))
    n = len(number_list)

    # 現在見ている桁数までをつなげたもの
    # すなわち、考えうる値の最大値
    high = 0
    DP = [0]*n
    for deg in range(n-1):
        # 1. 新たに追加される1桁の数
        # 1～9のうち、題意を満たすものを加算
        # 初回はこの処理が走らない
        if deg >= 1:
            DP[deg+1] += 7  # 4, 9以外の1～9の数値を加算

        # 2. 既に確定している数値の末尾に、0～9を追加
        DP[deg+1] += DP[deg] * 8  # 4, 9 以外の0～9を追加

        # 3.highから生成
        # high*10～high*10+number[deg+1]-1について追加
        nex_val = number_list[deg+1]
        # 3.1 0を追加
        # highが0の場合、0を追加しても0のままでおかしくなるので、初回はこの処理は走らない
        if deg >= 1:
            # hign*10が題意を満たす場合のみ、0を追加できる
            if str(high).count('4') + str(high).count('9') == 0:
                if nex_val >= 1:
                    DP[deg+1] += 1
        # 3.2 1～9を追加
        if nex_val >= 2:
            # high*10+値が題意を満たす場合のみ、追加できる
            if str(high).count('4') + str(high).count('9') == 0:
                # nex_valが1, ...,3の場合、そのまま追加
                if nex_val <= 4:
                    DP[deg+1] += nex_val - 1  # 3.1で処理している分、1を引く
                elif nex_val <= 9:
                    DP[deg+1] += nex_val - 2
                else:
                    raise

        # 次に進む
        high *= 10
        high += nex_val

    # 0とhighを追加
    # 4.1 0について処理
    DP[n-1] += 1  # 今回は0は常に題意を満たす
    # 4.2 highについて処理
    if str(high).count('4') + str(high).count('9'):
        pass
    else:
        DP[n-1] += 1
    ans = DP[n-1]
    return ans


main()
