# 各bit毎に、k個以上の1が存在するか
# 各bit毎に、1がたっている数をlistで保持する
# 1がたっている数がk個以上となる最大のbitを探す
from collections import Counter


def main():
    n, k = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    n += 1
    for i in range(1, n):
        A[i] += A[i-1]

    num_list = []

    for le in range(n):
        for ri in range(le+1, n):
            num = A[ri] - A[le]
            num_list.append(num)

    max_num = max(num_list)
    max_num_bit = bin(max_num)[2:]
    cnt_of = Counter(num_list)
    ans = 0
    for i in reversed(range(len(max_num_bit)+1)):
        bit = 1 << i
        # bit & num == 1となる数がk個以上あれば、このbitを採用し
        # bit & num == 1とならないものを取り除く
        if cnt_bit(cnt_of, bit) >= k:
            ans |= bit
            remove(cnt_of, bit)
    print(ans)


def cnt_bit(cnt_of, bit):
    ret = 0
    for key, val in cnt_of.items():
        if key & bit == bit:
            ret += val
    return ret


def remove(cnt_of, bit):
    del_list = []
    for key, val in cnt_of.items():
        if key & bit != bit:
            del_list.append(key)
    for key in del_list:
        cnt_of.pop(key)


main()
