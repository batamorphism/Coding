def rotate(S):
    return list(zip(*S[::-1]))  # zip(*L)で転置。転置+反転=回転


def find_top(S):
    for i, row in enumerate(S):
        for j, s in enumerate(row):
            if s == '#':
                return i, j


def is_same(S, T):
    si, sj = find_top(S)
    ti, tj = find_top(T)
    offset_i = ti-si
    offset_j = tj-sj
    n = len(S)
    for i, row in enumerate(S):
        for j, s in enumerate(row):
            ii = i+offset_i
            jj = j+offset_j
            if 0 <= ii < n and 0 <= jj < n:
                if s != T[ii][jj]:
                    return False
            else:
                if s == '#':
                    return False
    return True


def main():
    n = int(input())
    S = [input() for _ in range(n)]
    T = [input() for _ in range(n)]

    cnt_s = sum([1 for i in range(n) for j in range(n) if S[i][j] == '#'])
    cnt_t = sum([1 for i in range(n) for j in range(n) if T[i][j] == '#'])
    if cnt_s != cnt_t:
        print('No')
        return

    for _ in range(4):
        if is_same(S, T):
            print('Yes')
            return
        S = rotate(S)

    print('No')
    return


main()
