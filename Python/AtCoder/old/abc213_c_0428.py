# 座圧
def main():
    r_end, c_end, n = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]

    A = [a for a, b in AB]
    B = [b for a, b in AB]

    zipper_A = {a: i for i, a in enumerate(sorted(list(set(A))))}
    zipper_B = {b: i for i, b in enumerate(sorted(list(set(B))))}
    A = [zipper_A[a] for a in A]
    B = [zipper_B[b] for b in B]
    for a, b in zip(A, B):
        print(a+1, b+1)


main()
