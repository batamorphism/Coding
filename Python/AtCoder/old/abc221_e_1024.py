bit_end = 3*10**5+10
Data = [0]*(bit_end+10)
mod = 998244353
rev2 = (mod+1)//2

def add(pos, x):
    pos += 1
    while pos < bit_end:
        Data[pos] += x
        Data[pos] %= mod
        pos += pos & -pos


def getsum(pos):
    pos += 1
    ret = 0
    while pos > 0:
        ret += Data[pos]
        ret %= mod
        pos -= pos & -pos
    return ret


def main():
    n = int(input())
    A = list(map(int, input().split()))
    # A[k]が右端のものを考える
    # A[0]が左端の時、
    # A[0] <= A[k]ならば、2**(k-1)
    # A[1]が左端の時
    # A[1] <= A[k]ならば、2**(k-1-1)
    # A[i]が左端の時
    # A[i] M= A[k]ならば、2**(k-1-i)
    # したがって、各A[i]に対し、2**(-i)を入れておいて
    # A[k]を見るときは、A[i]以下の値の2**(-i)の合計をとってくればよい

    # 座標圧縮
    A_comp = {a: i for i, a in enumerate(sorted(list(set(A))))}
    A = [A_comp[a] for a in A]

    ans = 0
    for k, a in enumerate(A):
        x = getsum(a)
        # cnt = 2**(k-1)*x
        if k-1 < 0:
            cnt = 0
        else:
            cnt = pow(2, k-1, mod)*x
        ans += cnt
        ans %= mod
        # add(a, 2**(-k))
        add(a, pow(rev2, k, mod))

    print(ans)


main()
