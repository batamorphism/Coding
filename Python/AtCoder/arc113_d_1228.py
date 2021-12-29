# Aで考えられるのは
# c_end == 1とすると
# (r, c) = A[r]
# したがって、答えはk**r_end
# r_end == 1とすると
# (r, c) = B[c]
# したがって、答えはk**c_end
# c_end , r_end >= 2とする
# max(A) <= min(B)が必要
# 逆に、これを満たしていれば
mod = 998244353


def main():
    r_end, c_end, k = map(int, input().split())
    ans = 0
    if c_end == 1:
        ans = pow(k, r_end, mod)
    elif r_end == 1:
        ans = pow(k, c_end, mod)
    else:
        for a_max in range(1, k+1):
            a_cnt = pow(a_max, r_end, mod) - pow(a_max-1, r_end, mod)
            b_cnt = pow(k-a_max+1, c_end, mod)
            ans += a_cnt * b_cnt
            ans %= mod

    print(ans)


main()
