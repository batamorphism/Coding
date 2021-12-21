# https://atcoder.jp/contests/typical90/submissions/24060687
# https://algo-logic.info/segment-tree/

W, N = map(int, input().strip().split())
k = 1
while k < W:
    k *= 2

seg = [0 for _ in range(2*k)]
lazy = [-1 for _ in range(2*k)]


def _eval(i):
    # 遅延評価
    # 親から子に一世代伝播させ、親自体は更新済みフラグ(-1)を立てる
    if lazy[i] == -1:
        return

    if i < k - 1:
        lazy[2*i+1] = lazy[i]
        lazy[2*i+2] = lazy[i]

    seg[i] = lazy[i]
    lazy[i] = -1


def _sub_query(a, b, i, l, r):
    _eval(i)  # 遅延評価
    if r <= a or b <= l:
        return -1
    elif a <= l and r <= b:
        return seg[i]
    else:
        mid = l + (r - l) // 2
        vl = _sub_query(a, b, 2*i+1, l, mid)
        vr = _sub_query(a, b, 2*i+2, mid, r)
        return max(vl, vr)


def query(a, b):
    # [a, b)の最大値を返す
    return _sub_query(a, b, 0, 0, W)


def _sub_update(a, b, x, i, l, r):
    """[a, b)の値を更新する

    Args:
        a ([type]): 左端
        b ([type]): 右端
        x ([type]): 更新する値
        i ([type]): 現在参照しているnode
        l ([type]): 現在参照しているnodeの左端
        r ([type]): 現在参照しているnodeの右端
    """
    _eval(i)  # 遅延評価
    if a <= l and r <= b:  # 完全に内側の時
        lazy[i] = x
        _eval(i)  # segの値を更新するためにコール
    elif a < r and l < b:  # 一部分が内側の時
        mid = l + (r - l) // 2
        _sub_update(a, b, x, 2*i+1, l, mid)
        _sub_update(a, b, x, 2*i+2, mid, r)
        seg[i] = max(seg[2*i+1], seg[2*i+2])


def update(a, b, x):
    # [a, b)の値を更新する
    _sub_update(a, b, x, 0, 0, W)


# def build(array):
#     for i in range(N):
#         seg[i+k-1] = array[i]
#
#     for i in reversed(range(0, k-1)):
#         seg[i] = max(seg[2*i+1], seg[2*i+2])


def main():
    for _ in range(N):
        l, r = map(int, input().strip().split())
        tmp_max = query(l-1, r)
        update(l-1, r, tmp_max+1)
        print(tmp_max+1)


main()
