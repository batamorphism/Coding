def main():
    n = int(input())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # grundy = 0の時後攻必勝
    grundy = [[-1]*1326 for _ in range(51)]
    grundy[0][0] = 0
    grundy[0][1] = 0

    for i in range(51):
        for j in range(1326-50):
            if i == 0 and j <= 1:
                continue
            nex = set(grundy[i][j-j//2:j])
            if i > 0:
                nex.add(grundy[i-1][j+i])
            grundy[i][j] = min(set(range(max(nex)+2)) - nex)

    ans = 0
    for i in range(n):
        ans ^= grundy[W[i]][B[i]]

    if ans == 0:
        print('Second')
    else:
        print('First')


main()
