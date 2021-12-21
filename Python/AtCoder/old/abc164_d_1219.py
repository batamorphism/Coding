from collections import defaultdict


# Sのi文字目まで見た数をnum[i]とする
# 2019を法として考える
# Sのlo+1文字目からhi文字目までからなる数字は
# num[hi]-num[lo] // (10**(lo-1))
# 0 <= lo < hi <= len(S)
# 10と2019は互いに素であるから
# num[hi] = num[lo]と同値
# 各hiに対し、題意を満たすloの数の合計が答え
def main():
    S = input()

    mod = 2019
    n = len(S)
    num = [0]*(n+1)
    for i, char in enumerate(S[::-1], 1):
        num[i] = num[i-1] + int(char)*pow(10, (i-1), mod)
        num[i] %= mod

    # print(num)
    cnt_of = defaultdict(int)
    ans = 0
    for num_hi in num:
        ans += cnt_of[num_hi]
        cnt_of[num_hi] += 1

    print(ans)


main()
