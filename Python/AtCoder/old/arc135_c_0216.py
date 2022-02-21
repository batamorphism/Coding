# 操作回数は、0回か1回かいずれかしかない
def main():
    n = int(input())
    A = list(map(int, input().split()))
    # 各a_iに対し、sum(A^a_i)が計算できれば良い
    # 各bitに対し、bitの出現回数をcnt_of[bit]とすれば
    # cnt_of[bit]*(1<<bit)の総和を求めればよい
    cnt_of = [0]*30

    for bit in range(30):
        for a in A:
            if a >> bit & 1:
                cnt_of[bit] += 1

    ans = sum(A)
    for a_i in A:
        cur_ans = 0
        for bit in range(30):
            bit_a_i = a_i >> bit & 1
            if bit_a_i:
                cur_ans += (n-cnt_of[bit]) * (1 << bit)
            else:
                cur_ans += cnt_of[bit] * (1 << bit)
        ans = max(ans, cur_ans)
    print(ans)


main()
