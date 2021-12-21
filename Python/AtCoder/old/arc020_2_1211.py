# 色は1～10の10通り
# したがって、縞の選び方は、10*9=90通り

def main():
    n, c = map(int, input().split())
    A = [int(input()) for _ in range(n)]

    ans = float('inf')
    for col1 in range(1, 11):
        for col2 in range(1, 11):
            if col1 == col2:
                continue
            ans = min(ans, calc_cost(A, c, col1, col2))
    print(ans)


def calc_cost(A, c, col1, col2):
    # 奇数行をcol1、偶数行をcol2とする
    ret = 0
    for i, a_i in enumerate(A, 1):
        if i % 2 == 1:
            if a_i != col1:
                ret += c
        else:
            if a_i != col2:
                ret += c
    return ret


main()
