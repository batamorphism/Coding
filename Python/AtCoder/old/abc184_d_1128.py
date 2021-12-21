# 100^3 = 10**6
# ope_cnt(a, b, c) := 現在a, b, c枚あるときの、残りの操作回数
# a == 100 or b == 100 or c == 100のとき、0
def main():
    a, b, c = map(int, input().split())
    ans = ope_cnt(a, b, c)
    print(ans)


memo = {}
def ope_cnt(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)]
    if a == 100 or b == 100 or c == 100:
        return 0
    all = a+b+c
    prob_a = a/all
    prob_b = b/all
    prob_c = c/all
    ret = 0
    ret += prob_a*(ope_cnt(a+1, b, c)+1)
    ret += prob_b*(ope_cnt(a, b+1, c)+1)
    ret += prob_c*(ope_cnt(a, b, c+1)+1)
    memo[(a, b, c)] = ret
    return ret


main()
