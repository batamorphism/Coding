def main():
    h, w, k, v = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h)]
    B = [[0]*(w+1) for _ in range(h+1)]
    for r in range(1, h+1):
        for c in range(1, w+1):
            B[r][c] = B[r-1][c]+B[r][c-1]-B[r-1][c-1]+A[r-1][c-1]

    # 全探索
    ans = 0
    for r_0 in range(h):
        for c_0 in range(w):
            for r_1 in range(r_0, h):
                for c_1 in range(c_0, w):
                    area_size = (r_1-r_0+1)*(c_1-c_0+1)
                    if area_size <= ans:
                        continue
                    cost = calc_cost(B, k, r_0, c_0, r_1, c_1)
                    if cost <= v:
                        ans = max(area_size, ans)
    print(ans)


def calc_cost(B: list, k: int, r0: int, c0: int, r1: int, c1: int) -> int:
    # c0r0, c1r1の範囲のコストを計算する
    cost_1 = B[r1+1][c1+1]-B[r0][c1+1]-B[r1+1][c0]+B[r0][c0]
    cells_count = (r1-r0+1)*(c1-c0+1)
    cost_2 = cells_count*k
    return cost_1+cost_2


main()
