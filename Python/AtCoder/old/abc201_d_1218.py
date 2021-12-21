# ミニマックス法
# Takaはpotを最大化するように行動
# Aokiはpotを最小化するように行動
# DP[r][c] は上記行動に従った場合の、pot

def main():
    r_end, c_end = map(int, input().split())
    grid = [list(input()) for _ in range(r_end)]

    INF = float('inf')
    DP = [[0]*c_end for _ in range(r_end)]

    def calc_val(r, c):
        if grid[r][c] == '+':
            return 1
        else:
            return -1

    for r in range(r_end-1, -1, -1):
        for c in range(c_end-1, -1, -1):
            if r == r_end-1 and c == c_end-1:
                DP[r][c] = 0
                continue
            if (r+c) % 2 == 0:
                # Taka Turn
                # potを最大化する
                pot = -INF
                if r < r_end-1:
                    pot = max(pot, DP[r+1][c]+calc_val(r+1, c))
                if c < c_end-1:
                    pot = max(pot, DP[r][c+1]+calc_val(r, c+1))
            else:
                # Aoki Turn
                # potを最小化する
                pot = INF
                if r < r_end-1:
                    pot = min(pot, DP[r+1][c]-calc_val(r+1, c))
                if c < c_end-1:
                    pot = min(pot, DP[r][c+1]-calc_val(r, c+1))
            DP[r][c] = pot

    pot_last = DP[0][0]

    if pot_last > 0:
        print('Takahashi')
    elif pot_last < 0:
        print('Aoki')
    else:
        print('Draw')


main()
