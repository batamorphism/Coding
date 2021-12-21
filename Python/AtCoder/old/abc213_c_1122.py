def main():
    _, _, n = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 座標圧縮
    zipper_A = {a: i for i, a in enumerate(sorted(list(set(A))))}
    zipper_B = {b: i for i, b in enumerate(sorted(list(set(B))))}

    # 座標圧縮後のA, Bを作成
    zip_A = [zipper_A[a] for a in A]
    zip_B = [zipper_B[b] for b in B]

    for a, b in zip(zip_A, zip_B):
        print(a+1, b+1)


main()
