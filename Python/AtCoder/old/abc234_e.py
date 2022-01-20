# 条件1: 数列の長さ=桁数が最小であること
# 条件2: d1が最小であること
# 条件3: 差がー
# まず、xが10桁以上である場合、等差数とは連番以外存在しない
# 10桁以下の場合、全部見ればよい
def main():
    x = int(input())
    x_str = str(x)
    deg = len(x_str)
    if deg >= 11:
        ans = solve1(x)
    else:
        ans = solve2(x)
    print(ans)


def solve1(x):
    # xを超える最大の連番を求める
    x_str = str(x)
    deg = len(x_str)
    hi = int(x_str[0])
    if hi == 9:
        ans = int(str(hi)*deg)
    else:
        ans1 = int(str(hi)*deg)
        ans2 = int(str(hi+1)*deg)
        if ans1 < x:
            ans = ans2
        else:
            ans = ans1
    return ans


def solve2(x):
    x_str = str(x)
    deg = len(x_str)
    # make 等差数字
    ans = float('inf')
    for d in [deg, deg+1]:
        for d1 in range(1, 10):
            for diff in range(-9, 10):
                val = []
                d_i = d1
                for _ in range(d):
                    # 今の先頭の数字を更新
                    val.append(str(d_i))
                    d_i = d_i + diff
                    if not (0 <= d_i <= 9):
                        break
                val_int = int(''.join(val))
                if val_int >= x:
                    ans = min(ans, val_int)
    return ans


main()
