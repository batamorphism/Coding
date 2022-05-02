from collections import defaultdict
from functools import lru_cache


# bitDP
# i番目まで見たとき、Sを使っていてかつ条件を満たすものの数
def main():
    n, m = map(int, input().split())
    cond_of = defaultdict(list)
    for _ in range(m):
        x, y, z = map(int, input().split())
        y -= 1
        cond_of[x].append((y, z))

    def check(i, S):
        cond = cond_of[i]
        if not cond:
            return True
        for y, z in cond:
            # Sの中に、y以下の数がz個以下しか存在しなければok
            mask = (1 << (y+1)) - 1
            leq_S = S & mask
            cnt = popcount(leq_S)
            if cnt > z:
                return False
        return True

    S_end = 1 << n
    DP = [0] * S_end
    DP[0] = 1
    for pre_S in range(S_end):
        if DP[pre_S] == 0:
            continue
        pre_i = popcount(pre_S)
        for a_i in range(n):
            if (pre_S >> a_i) & 1:
                continue
            cur_i = pre_i + 1
            cur_S = pre_S | (1 << a_i)
            # cur_iとcur_Sが条件を満たしていれば、加算できる
            if check(cur_i, cur_S):
                DP[cur_S] += DP[pre_S]

    ans = DP[-1]
    print(ans)


@lru_cache(maxsize=None)
def popcount(S):
    return bin(S).count('1')


main()
