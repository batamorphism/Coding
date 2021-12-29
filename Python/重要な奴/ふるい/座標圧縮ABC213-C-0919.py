def main():
    n, w, n = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 座標圧縮では、元の集合をsortして
    # 要素に対する順位の辞書を作るのが典型
    A_sorted = sorted(set(A))
    A_dict = {a: i for i, a in enumerate(A_sorted)}

    B_sorted = sorted(set(B))
    B_dict = {b: i for i, b in enumerate(B_sorted)}

    for a, b in zip(A, B):
        print(A_dict[a]+1, B_dict[b]+1)


main()
