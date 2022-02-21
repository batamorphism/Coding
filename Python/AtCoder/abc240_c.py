# DP
def main():
    n, x = map(int, input().split())
    jump_list = [tuple(map(int, input().split())) for _ in range(n)]

    DP = [False]*(x+1)
    DP[0] = True
    for a, b in jump_list:
        new_DP = [False]*(x+1)
        for cur_x in range(x+1):
            if DP[cur_x]:
                nex_x = cur_x + a
                if nex_x <= x:
                    new_DP[nex_x] = True
                nex_x = cur_x + b
                if nex_x <= x:
                    new_DP[nex_x] = True
        DP = new_DP[:]

    ans = DP[x]
    if ans:
        print('Yes')
    else:
        print('No')


main()
