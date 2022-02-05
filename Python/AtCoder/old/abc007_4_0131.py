# 桁DP

def main():
    a, b = map(int, input().split())
    cnt_a = solve(a-1)
    cnt_b = solve(b)
    ans = cnt_b - cnt_a
    ans = b-a+1-ans
    print(ans)


def val_gen():
    yield from range(4)
    yield from range(5, 9)


def solve(n):
    # 1以上n以下の整数であり、4と9を含まない数がいくつあるか
    if n == 0:
        return 0
    number_list = list(map(int, str(n)))
    DP = [0] * (len(number_list) + 1)
    top_val_S = 0

    # 配るDP
    for i in range(len(number_list)):
        # 1. この桁から始まる1桁の数
        if i != 0:
            for val in val_gen():
                if val == 0:
                    continue
                DP[i+1] += 1
        # 2. 前の桁の末尾に数を追加
        for val in val_gen():
            DP[i+1] += DP[i]
        # 3. top_valから連鎖
        nex_val = number_list[i]
        if (top_val_S >> 4 & 1 == 0) and (top_val_S >> 9 & 1 == 0):
            for val in val_gen():
                if i == 0:
                    if val == 0:
                        continue
                if val >= nex_val:
                    continue
                DP[i+1] += 1
        top_val_S |= 1 << nex_val

    # top_valについて処理
    if (top_val_S >> 4 & 1 == 0) and (top_val_S >> 9 & 1 == 0):
        DP[len(number_list)] += 1

    ans = DP[len(number_list)]
    return ans


main()
