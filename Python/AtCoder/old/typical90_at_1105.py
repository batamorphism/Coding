# mod 46で考え、0~45の数値がそれぞれいくつあるか考える
# A, B, Cの全ての組み合わせは46**3 = 97336通りしかないので、全探索する
mod = 46


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A_zip = [0]*mod
    B_zip = [0]*mod
    C_zip = [0]*mod
    for a in A:
        A_zip[a % mod] += 1
    for b in B:
        B_zip[b % mod] += 1
    for c in C:
        C_zip[c % mod] += 1

    ans = 0
    for a, a_cnt in enumerate(A_zip):
        for b, b_cnt in enumerate(B_zip):
            for c, c_cnt in enumerate(C_zip):
                if (a+b+c) % mod == 0:
                    ans += a_cnt*b_cnt*c_cnt

    print(ans)


main()
