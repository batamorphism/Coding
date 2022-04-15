from collections import defaultdict
from collections import deque
import copy
MOD = 998244353


def main():
    n, k = map(int, input().split())
    bit_list = []
    for _ in range(n):
        S = input()
        A = set(c2i(c) for c in S)
        bit = 0
        for i in range(26):
            if i in A:
                bit |= 1 << i
        bit_list.append(bit)

    nei_of = defaultdict(set)
    rev_nei_of = defaultdict(set)
    node_set = set()
    root_set = set()
    # 親として、共通部分からなるbitを持つ木を考える
    # 親の組み合わせ数分が重複するので、求めるべきは
    # 子の組み合わせ数全体から、親の組み合わせ数を引いたものが新野答えとなる
    ALL = 1 << n
    for S in range(ALL):
        child_list = set()
        and_bit = -1
        for i in range(n):
            if (S >> i) & 1 == 0:
                continue
            child_list.add(bit_list[i])
            and_bit &= bit_list[i]
        if and_bit == -1:
            continue
        # and_bitがbit_list[S]の親となる
        # print(bin(S), and_bit, child_list)
        for child in child_list:
            if child == and_bit:
                continue
            nei_of[and_bit].add(child)
            node_set.add(child)
            rev_nei_of[child].add(and_bit)

    cnt_of = defaultdict(int)
    used = defaultdict(int)
    # bit_listにあるものが葉である
    # 葉から探索していき、それ以上先がない奴がroot
    for leaf in bit_list:
        que = [leaf]
        while que:
            pre = que.pop()
            pc = bin(pre).count('1')
            # pc種類からk個選ぶので pc**k
            cnt_of[pre] = pow(pc, k, MOD)
            # cnt_of[pre] = pow(pc, k)
            is_root = True
            for cur in rev_nei_of[pre]:
                is_root = False
                if used[cur] == 0:
                    que.append(cur)
                    used[cur] = 1
            if is_root and pre != 0:
                root_set.add(pre)
    # print(root_set)
    ans_cnt_of = copy.deepcopy(cnt_of)
    used = defaultdict(int)
    for root in root_set:
        que = [root]
        if used[root]:
            raise
        used[root] = 1
        while que:
            pre = que.pop()
            for cur in nei_of[pre]:
                if used[cur] == 0:
                    for pre2 in rev_nei_of[cur]:
                        ans_cnt_of[cur] -= cnt_of[pre2]
                    que.append(cur)
                    used[cur] = 1

    ans = sum(ans_cnt_of.values())
    ans %= MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('a')


main()
