# 2行2列のものに対し
#   4 5 <-max
# 1 1 5
# 2 4 2
# ^min
# Aは各行の最小値、
# Bは各列の最大値
# min(B) >= max(A)であれば、あらゆるパターンを作成できる
# min(B) = min_Bとして
# Bは、min_B <= b <= kからなる配列であって、min_B駆らなず含む数
# ->(k-min_B+1)**c_end - (k-min_B)**c_end個
# Aは、1 <= a <= min_Bからなる配列の個数
# ->min_B**r_end個
def main():
    r_end, c_end, k = map(int, input().split())
    MOD = 998244353

    if r_end == 1:
        ans = pow(k, c_end, MOD)
        print(ans)
        return
    elif c_end == 1:
        ans = pow(k, r_end, MOD)
        print(ans)
        return

    ans = 0
    for min_B in range(1, k+1):
        b_cnt = pow(k-min_B+1, c_end, MOD) - pow(k-min_B, c_end, MOD)
        a_cnt = pow(min_B, r_end, MOD)
        ans += b_cnt * a_cnt
        ans %= MOD
    print(ans)


main()
