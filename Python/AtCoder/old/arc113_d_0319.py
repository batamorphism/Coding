MOD = 998244353


def main():
    r_end, c_end, k = map(int, input().split())
    if r_end == 1:
        # c_end個に、1～k個の値を入れる
        ans = pow(k, c_end, MOD)
    elif c_end == 1:
        ans = pow(k, r_end, MOD)
    else:
        ans = solve(r_end, c_end, k)
    print(ans)


def solve(r_end, c_end, k):
    if r_end == 1 or c_end == 1:
        raise

    # max(A) <= min(B)を満たす数列は自由に作れる
    len_a = r_end
    len_b = c_end
    ans = 0

    for max_a in range(1, k+1):
        a_cnt = pow(max_a, len_a, MOD) - pow(max_a-1, len_a, MOD)
        b_cnt = pow(k-max_a+1, len_b, MOD)
        ans += a_cnt * b_cnt
        ans %= MOD
    return ans


main()
