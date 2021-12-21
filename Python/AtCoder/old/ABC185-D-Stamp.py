import math


def main():
    # input
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(m):  # 0スタートにする
        A[i] -= 1
    solv(n, m, A)


def solv(n: int, m: int, A: list):
    """solver
    左右方向一列にn個のマスが並んでいる
    左からi番目のマス(0<=i<n)のマスをマスiとする
    このn個のマスのうち、マスA[0],...,A[m-1]のm個のマスは青色
    それ以外のマスは白色

    ここで一度だけ、k>0を選んで幅kのハンコを作る
    幅kのハンコを使うと、連続するkマスを赤色に変えることができる
    ただしその際、そのk個の中に青色のマスが入っていてはならない

    最小で何回ハンコを使用すれば、白色のマスが存在しなくできるか

    n<=10**9
    m<2*10**5

    O(m)くらいでやりたい
    Aはあらかじめソートしておく
    連続したwhiteの数をk'とする
    k' = kのとき、1回
    k+1 <= k' <= 2*k のとき、2回
    2*k+1 <= k' <= 3*k のとき、3回

    Args:
        n (int): [description]
        m (int): [description]
        A (list): [description]
    """
    A.sort()

    # 2分探索
    # kは大きいほど回数が減る
    # ただし、大きすぎると、解がなくなる
    # k:1 2 3  4  5  6  7  8  9
    # a:9 5 2 -INF - -  -  -  -
    # kの値として考えうる範囲は、1～n
    # ここで、aが-INFになる直前の値を探す
    ok = 1
    ng = n+1
    while ng-ok >= 2:
        mid = (ok+ng)//2
        mid_ans = solv_with_k(n, m, A, mid)
        if mid_ans < 0:
            ng = mid
        else:
            ok = mid
    # 欲しいkが求まったので、このkの時のスタンプを押す回数が答え
    print(solv_with_k(n, m, A, ok))


def how_many_push(how_many_white, k):
    """how many push
    k' = kのとき、1回
    k+1 <= k' <= 2*k のとき、2回
    2*k+1 <= k' <= 3*k のとき、3回
    ただし、k'<kの時は解がないので、-INFを返す

    Args:
        how_many_white (int): [description]
        k (int): [description]
    """
    if how_many_white == 0:
        return 0
    elif how_many_white < k:
        return -10**24
    else:
        return math.ceil(how_many_white/k)


def solv_with_k(n: int, m: int, A: list, k:int) -> int:
    """kが固定された時の解を求める
    """
    pre_a = -1
    ans = 0
    for a in A:
        how_many_white = a-pre_a-1
        ans += how_many_push(how_many_white, k)
        pre_a = a
    how_many_white = n - pre_a-1
    ans += how_many_push(how_many_white, k)
    return ans


main()
