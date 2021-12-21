# 貪欲
def main():
    r_end, c_end = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r_end)]
    B = [list(map(int, input().split())) for _ in range(r_end)]

    # 0, 0から合わせていく
    ans = 0
    for r in range(r_end-1):
        for c in range(c_end-1):
            add = B[r][c] - A[r][c]
            ans += abs(add)
            A[r][c] += add
            A[r+1][c] += add
            A[r][c+1] += add
            A[r+1][c+1] += add

    same = (A == B)
    if same:
        print('Yes')
        print(ans)
    else:
        print('No')


main()
