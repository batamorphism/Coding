mod = 998244353
inv = (mod+1)//2
DATA_MAX = 10**6
DATA = [0]*(DATA_MAX+10)


def add(pos, x):
    while pos <= DATA_MAX:
        DATA[pos] += x
        pos += pos & -pos


def get_sum(pos):
    ans = 0
    while pos > 0:
        ans += DATA[pos]
        pos -= pos & -pos
    return ans


def main():
    n_end = int(input())
    n_end += 1
    n_begin = 1
    A = list(map(int, input().split()))
    A = [0]+A
    # 座標圧縮
    A_com = {n: i for i, n in enumerate(sorted(list(set(A))))}
    B = [A_com[a] for a in A]

    ans = 0
    for k in range(n_begin, n_end):
        b = B[k]
        ans_k = pow(2, k-1, mod)
        ans_k *= get_sum(b)  # A_1 <= A_kが条件で=が入るから、sum(b-1)ではなくsum(b)
        ans_k %= mod
        add(b, pow(inv, k, mod))
        ans += ans_k
        ans %= mod

    print(ans)


main()
