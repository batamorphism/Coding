# ビット毎に独立に考える?
# n <= 1000より、部分列の種類を全列挙できる
# 10**6個から、k個選んでandが最大となるようにする
# 最上位のbitから見ていって、1がk個以上あれば、0となっている数値は捨てる
# そして、答えのbitを1にする
from collections import Counter


def main():
    n, k = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    for i in range(n+1):
        A[i] += A[i-1]

    num_list = []
    for le in range(1, n+1):
        for ri in range(le, n+1):
            num = A[ri] - A[le-1]
            num_list.append(num)

    max_num = max(num_list)
    max_bit = len(bin(max_num)[2:])
    num_cnt = Counter(num_list)
    ans = 0
    for i in range(max_bit, -1, -1):
        bit = 1 << i
        # bit & num となる数がk個以上あれば、このbitを採用
        if cnt_bit(num_cnt, bit) >= k:
            ans |= bit
            remove(num_cnt, bit)
    print(ans)


def cnt_bit(num_cnt, bit):
    ret = 0
    for key, val in num_cnt.items():
        if key & bit:
            ret += val
    return ret


def remove(num_cnt, bit):
    del_key = []
    for key, val in num_cnt.items():
        if not(key & bit):
            del_key.append(key)
    for key in del_key:
        del num_cnt[key]


main()
