def main():
    n = int(input())
    A = list(map(int, input().split()))
    bit_end = 31

    # 考えうる数は
    # Aそのものと
    # 1回だけ操作したもの
    ans = sum(A)
    # 元のaに、各桁が何回登場するか
    cnt_of = [0]*bit_end
    for a_i in A:
        for bit in range(bit_end):
            if a_i >> bit & 1:
                cnt_of[bit] += 1

    for a_i in A:
        new_cnt_of = cnt_of[:]
        for bit in range(bit_end):
            if a_i >> bit & 1:
                new_cnt_of[bit] = n - new_cnt_of[bit]
        sum_ = 0
        for bit in range(bit_end):
            if new_cnt_of[bit]:
                sum_ += (1 << bit)*new_cnt_of[bit]
        ans = max(ans, sum_)
    print(ans)


main()
