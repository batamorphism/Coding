def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    A = [0] + A
    n += 1
    for i in range(1, len(A)):
        A[i] += A[i-1]

    num_list = []
    for ri in range(n):
        for le in range(ri):
            # [le, ri)の和を求める
            val = A[ri] - A[le]
            num_list.append(val)

    # num_listからk個選んで、andを計算した時の最大値を求める
    max_num = max(num_list)
    max_bit = 1
    while 1 << max_bit <= max_num:
        max_bit += 1

    # 上からbit毎に考え、1となる数がk個以上あれば、それを答えに加算
    ans = 0
    for bit in reversed(range(max_bit+1)):
        cnt = calc_cnt(num_list, bit)
        if cnt >= k:
            ans += 1 << bit
            remove_num(num_list, bit)
    print(ans)


def calc_cnt(num_list, bit):
    cnt = 0
    for num in num_list:
        if num & (1 << bit):
            cnt += 1
    return cnt


def remove_num(num_list, bit):
    # bitが0のものを除く
    for i, num in enumerate(num_list):
        if num & (1 << bit) == 0:
            num_list[i] = 0


main()
