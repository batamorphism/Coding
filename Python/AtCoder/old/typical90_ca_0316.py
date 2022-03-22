# 貪欲
def main():
    r_end, c_end = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r_end)]
    B = [list(map(int, input().split())) for _ in range(r_end)]

    # 左上から数値を合わせていく
    ans = 0
    for r in range(r_end-1):
        for c in range(c_end-1):
            a_rc = A[r][c]
            b_rc = B[r][c]
            delta = b_rc-a_rc
            ans += abs(delta)
            A[r][c] += delta
            A[r+1][c] += delta
            A[r][c+1] += delta
            A[r+1][c+1] += delta

    if A == B:
        print('Yes')
        print(ans)
    else:
        print('No')


main()
