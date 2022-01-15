from itertools import product


# ワーシャルフロイド
def main():
    r_end, c_end = map(int, input().split())

    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(r_end)]

    for k, fr, to in product(range(10), repeat=3):
        d1 = C[fr][k] + C[k][to]
        d2 = C[fr][to]
        C[fr][to] = min(d1, d2)

    cost = 0
    for r, c in product(range(r_end), range(c_end)):
        a_rc = A[r][c]
        if a_rc == -1:
            continue
        cost += C[a_rc][1]

    print(cost)


main()
