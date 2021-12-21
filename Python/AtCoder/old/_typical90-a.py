def main():
    n, L = map(int, input().split())
    k = int(input())
    A = list(map(int, input().split()))
    A.append(L)
    piece = []
    for i in range(n+1):
        if i == 0:
            piece.append(A[i])
        else:
            piece.append(A[i]-A[i-1])

    ok = 0
    ng = L+1
    while ng-ok > 1:
        mid = (ok+ng)//2
        if check(piece, mid, k+1):
            ok = mid
        else:
            ng = mid

    print(ok)


def check(piece, x, n):
    # pieceを長さx以上で分割していって
    # n個以上にできるか
    cnt = 0
    cur_piece = 0
    for i in range(len(piece)):
        cur_piece += piece[i]
        if cur_piece >= x:
            cur_piece = 0
            cnt += 1
    return cnt >= n


main()
