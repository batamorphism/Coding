def main():
    n, k = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    n += 1

    # 累積和
    for i in range(1, n):
        A[i] += A[i-1]

    bit_list = []
    for le in range(n):
        for ri in range(le+1, n):
            sum_ = A[ri] - A[le]
            bit_list.append(sum_)

    # print(bit_list)

    # 上から見ていって、k個以上あれば、それを採用し、その桁が0のものを消す
    max_number = max(bit_list)
    max_bit = bin(max_number)[2:]
    ans = 0
    for dgt in reversed(range(len(max_bit))):
        if cnt_of(bit_list, dgt) >= k:
            ans |= 1 << dgt
            remove(bit_list, dgt)

    print(ans)


def cnt_of(bit_list, dgt):
    # dgt桁目が1のものをカウント
    ret = 0
    for bit in bit_list:
        if bit >> dgt & 1:
            ret += 1
    return ret


def remove(bit_list, dgt):
    # dgt桁目が0のものを削除
    for i, bit in enumerate(bit_list):
        if bit >> dgt & 1 == 0:
            bit_list[i] = 0


main()
