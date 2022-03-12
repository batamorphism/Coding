def main():
    a, b = map(int, input().split())
    a -= 1
    # a以下の数値で禁止された数字がいくつあるか
    a_cnt = solve(a)
    b_cnt = solve(b)
    ans = b_cnt - a_cnt
    print(ans)


def solve(a):
    # a以下の数値で禁止された数字がいくつあるか
    # 0 <= aであるため、0もありうる
    # 禁止されていない数がいくつあるか数える
    # 桁DP
    if a == 0:
        return 0
    numbers = list(map(int, str(a)))
    dp = 0
    # top_val = 0
    top_S = set()
    for dgt in range(len(numbers)):
        new_dp = 0
        # 1. 1桁の数値 1~9のうち4, 9以外
        if dgt != 0:
            new_dp += (9-2)

        # 2. 既にある数値の末尾に0~9のうち4, 9以外を追加
        new_dp += dp*(10-2)

        # 3. top_valから連鎖
        # top_valが禁じされた数字でない場合にのみ、top_valを追加
        if dgt == 0:
            val_begin = 1
        else:
            val_begin = 0
        val_end = numbers[dgt]
        if not (4 in top_S or 9 in top_S):
            for val in range(val_begin, val_end):
                if val != 4 and val != 9:
                    new_dp += 1
        # 更新
        top_S.add(numbers[dgt])
        dp = new_dp

    # 4. 0と、top_valを処理
    dp += 1  # 0は禁止されていない
    if not (4 in top_S or 9 in top_S):
        dp += 1
    ans = (a+1)-dp
    return ans


main()
