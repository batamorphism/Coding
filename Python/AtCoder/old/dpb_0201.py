def main():
    n, k = map(int, input().split())
    # 累積和は1-indexed
    A = [0] + list(map(int, input().split()))
    n += 1

    for i in range(1, n):
        A[i] += A[i-1]

    # 美しさ全体を求める
    btf_list = []
    for le in range(n):
        for ri in range(le+1, n):
            # (le, ri] の累積和
            btf = A[ri] - A[le]
            btf_list.append(btf)

    # 一番大きい数よりでかい数は見る必要なし
    max_btf = max(btf_list)
    max_btf_bin = bin(max_btf)[2:]
    ans = 0
    # 左から順にbitを見ていく
    for dgt in reversed(range(len(max_btf_bin))):
        if cnt_bit_of_dgt(dgt, btf_list) >= k:
            # dgt桁目に1がたっている数がk個以上ある場合、採用
            ans += 1 << dgt
            remove(dgt, btf_list)

    print(ans)


def cnt_bit_of_dgt(dgt, btf_list):
    cnt = 0
    for btf in btf_list:
        if btf >> dgt & 1:
            cnt += 1
    return cnt


def remove(dgt, btf_list):
    for i, btf in enumerate(btf_list):
        if btf >> dgt & 1 == 0:
            btf_list[i] = 0


main()
