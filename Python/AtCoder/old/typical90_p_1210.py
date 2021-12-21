# コインDP -> TLE
# aとbを全探索
def main():
    n = int(input())
    a_val, b_val, c_val = map(int, input().split())

    ans = float('inf')
    for a_cnt in range(10000):
        val1 = a_cnt*a_val
        if val1 > n:
            break
        for b_cnt in range(10000):
            val2 = val1 + b_cnt*b_val
            if val2 > n:
                break
            val3 = n - val2
            if val3 % c_val == 0:
                c_cnt = val3 // c_val
                ans = min(ans, a_cnt + b_cnt + c_cnt)

    print(ans)


main()
