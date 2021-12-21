from collections import deque

h = 0
w = 0

# 01BFS
# 幅優先探索について、コスト0の場合は深さ優先、コスト1の場合は幅優先とする事で、
# コストが最小のものを取得できる

def main():
    global h, w
    h, w = map(int, input().split())
    S = []
    Dist = [[10**10]*w for _ in range(h)]  # 距離
    for _ in range(h):
        S.append(list(*input().split()))

    q = deque()
    q.appendleft((0, 0))
    Dist[0][0] = 0

    # Start 01 BFS
    while q:
        r, c = q.popleft()

        # コスト0で移動できる方の処理
        to0 = get_neighbor_dist0(r, c)  # r, cの近傍を取得
        for rr, cc in to0:
            if is_inside(rr, cc):  # 枠に入っているかは別途用の関数を作るのが良い
                if Dist[rr][cc] > Dist[r][c]:  # 距離が更新できる場合のみ更新
                    if S[rr][cc] != '#':  # コスト0で移動できる場合
                        Dist[rr][cc] = Dist[r][c]
                        q.appendleft((rr, cc))  # 左側に追加し、コスト0を優先、つまり深さ優先

        # コスト1で移動できる方の処理
        to1 = get_neighbor_dist1(r, c)
        for rr, cc in to1:
            if is_inside(rr, cc):
                if Dist[rr][cc] > Dist[r][c]+1:
                    Dist[rr][cc] = Dist[r][c]+1
                    q.append((rr, cc))  # 右側に追加し、コスト1は後から処理する、つまり幅優先

    print(Dist[-1][-1])


def is_inside(r, c):
    global h, w
    if 0 <= r < h and 0 <= c < w:
        return True
    return False


def get_neighbor_dist0(r, c):
    # .*.
    # *.*
    # .*.
    A = []
    Arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for a in Arr:
        A.append((r+a[0], c+a[1]))
    return A


def get_neighbor_dist1(r, c):
    # .***.
    # *****
    # **@**
    # *****
    # .***.
    A = []
    Arr = ([
            (-1, 2), (0, 2), (1, 2),
            (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
            (-2, 0), (-1, 0), (1, 0), (2, 0),
            (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
            (-1, -2), (0, -2), (1, -2),
            ])
    for a in Arr:
        A.append((r+a[0], c+a[1]))
    return A


main()