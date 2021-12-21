def main():
    h, w, n = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 座標圧縮
    A_dict = {a: i for i, a in enumerate(sorted(list(set(A))))}
    B_dict = {b: i for i, b in enumerate(sorted(list(set(B))))}
    A_comp = [A_dict[a] for a in A]
    B_comp = [B_dict[b] for b in B]
    for a_c, b_c in zip(A_comp, B_comp):
        print(a_c+1, b_c+1)
    return 1


main()
