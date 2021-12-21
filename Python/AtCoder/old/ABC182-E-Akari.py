def main():
    h, w, n, m = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    C = []
    D = []
    for _ in range(m):
        c, d = map(int, input().split())
        C.append(c-1)
        D.append(d-1)
    solv(h, w, n, m, A, B, C, D)


def solv(h: int, w: int, n: int, m: int, A: list, B: list, C: list, D: list):
    """h行w列のマス目がある
    電球は(A[i],B[i])に置かれている
    ブロックは(C[i], D[i])におかれている
    電球は光を上下左右4方向に放つ。ただし、ブロックが置かれているとさえぎられる
    光が届くマスの合計をもとめよ
    
    ぎりぎり全マスに対する全探索は可能
    電球は10**5なので、全電球に対する全探索も可能
    
    Args:
        h (int): [description]
        w (int): [description]
        n (int): [description]
        m (int): [description]
        A (list): [description]
        B (list): [description]
        C (list): [description]
        D (list): [description]
    """
    # Blocks[r][c]
    # '.':floor
    # '#':wall
    # '*':light
    # init Blocks and set wall
    Blocks = [['.']*w for _ in range(h)]
    Blocks_w = [['.']*w for _ in range(h)]
    Blocks_h = [['.']*w for _ in range(h)]
    for (c, d) in zip(C, D):
        Blocks_w[c][d] = '#'
        Blocks_h[c][d] = '#'
        Blocks[c][d] = '#'
    for (a, b) in zip(A, B):
        # 横方向
        if Blocks_w[a][b] == '*':
            continue
        # 右側を*で埋める
        for col in range(b, w):
            if Blocks_w[a][col] == '#':
                break
            Blocks_w[a][col] = '*'
        # 左側を*で埋める
        for col in range(b, -1, -1):
            if Blocks_w[a][col] == '#':
                break
            Blocks_w[a][col] = '*'
    for (a, b) in zip(A, B):
        # 縦方向
        if Blocks_h[a][b] == '*':
            continue
        # 下側を*で埋める
        for row in range(a, h):
            if Blocks_h[row][b] == '#':
                break
            Blocks_h[row][b] = '*'
        # 上側を*で埋める
        for row in range(a, -1, -1):
            if Blocks_h[row][b] == '#':
                break
            Blocks_h[row][b] = '*'

    for row in range(h):
        for col in range(w):
            if Blocks_w[row][col] == '*' or Blocks_h[row][col] == '*':
                Blocks[row][col] = '*'

    ans = 0
    for row in Blocks:
        ans += row.count('*')
    print(ans)


def print_list(A: list):
    for a in A:
        print(a)


main()
