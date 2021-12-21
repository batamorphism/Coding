def solver(n: int, m: int, H: list, W: list):
    """solver
    DP[i]を、iが偶数の時は、H[0]～H[i]と、あるH[i]以下のW[j]のペアで最小のもの
    奇数の時はH[0]～H[i]のペアで最小のものとする
    HとWをあらかじめソートしておけば、順番にH[1]-H[0]+H[2]-H[1],...しておけばよい
    DP[2*i] = DP[2*i-2]+H[2*i]-H[2*i-1]か（2*i-1～2*iにあるwを無視する場合）
    DP[2*i-1] + abs(H[2*i]-W) (ここでH[2*i-1]<=W<H[2*i])か（2*i-1～2*iにあるwに変身する場合）
    DP[2*i-3] + abs(H[2*i-2]-W) + H[2*i]-H[2*i-1]  (ここでH[2*i-2]<=W<H[2*i-1])（2*i-2～2*i-1にあるwに変身する場合）
    ここで、
    DP[0] = abs(w-H[0]) ここでwは最もH[0]に近いもの
    DP[1] = H[1]-H[0]
    DP[2] = DP[2*i-2]+H[2*i]-H[2+i-1]か
            DP[2*i-1] + abs(H[2*i]-W)（第3項は気にしなくてよい)

    Args:
        n (int): [description]
        m (int): [description]
        H (list): [description]
        W (list): [description]
    """
    H.sort()
    W.sort()
    DP = [-1]*n
    for i in range(n):
        # いまいちっぽい点(1)
        # iが小さいときの条件分岐が多い
        if i == 0:
            # いまいちっぽい点(2)
            # H[0]に最も近いwを取得して処理しようとしているが、煩雑
            w_list1 = get_w_list(W, 0, H[i])
            w_list2 = get_w_list(W, H[i], 10**30)
            DP[i] = min(abs(w_list1[-1]-H[0]), abs(w_list2[0]-H[0]))
            continue
        if i == 1:
            DP[i] = H[1] - H[0]
            continue
        if i == 2:
            pre_dp1 = DP[i-2]+H[i]-H[i-1]
            pre_dp2 = 10**30
            w_list = get_w_list(W, H[i-1], H[i])
            for w in w_list:
                pre_pre_dp2 = DP[i-1] + abs(H[i]-w)
                if pre_dp2 > pre_pre_dp2:
                    pre_dp2 = pre_pre_dp2
            DP[i] = min(pre_dp1, pre_dp2)
            continue

        if i % 2 == 0:
            # いまいちっぽい点(3)
            # pre_* であったり、pre_pre_*であったり、命名がいまいち
            # いまいちっぽい点(4)
            # pre_dp1,...,pre_dp3の最小値をとっている処理が煩雑っぽい
            # いまいちっぽい点(5)
            # H[i-1]～H[i]に含まれるWの部分列をget_w_listで取得しているが、
            # H[i]に最も近いWの要素を取得して組んだ方が良かったりするか？
            pre_dp1 = DP[i-2]+H[i]-H[i-1]
            pre_dp2 = 10**30
            w_list = get_w_list(W, H[i-1], H[i])
            for w in w_list:
                pre_pre_dp2 = DP[i-1] + abs(H[i]-w)
                if pre_dp2 > pre_pre_dp2:
                    pre_dp2 = pre_pre_dp2
            pre_dp3 = 10**30
            w_list = get_w_list(W, H[i-2], H[i-1])
            for w in w_list:
                pre_pre_dp3 = DP[i-3]+abs(H[i-2]-w)+H[i]-H[i-1]
                if pre_dp3 > pre_pre_dp3:
                    pre_dp3 = pre_pre_dp3
            DP[i] = min(pre_dp1, pre_dp2, pre_dp3)
        else:
            DP[i] = DP[i-2]+H[i]-H[i-1]

    # DP[n-1]は、H[n-1]より大きいWを反映できていない
    # したがって、別途処理する...超いまいち
    # いまいちっぽい点(6)
    # 別途処理しているので間違いやすい(ここで2回WAした)
    w_list = get_w_list(W, H[n-1], 10**30)
    pre_dp = DP[n-2] + abs(w_list[0] - H[n-1])
    if DP[n-1] > pre_dp:
        DP[n-1] = pre_dp

    return DP[-1]


def get_w_list(W: list, low: int, high: int) -> list:
    """
    ソートされたリストwの部分列で要素がlow以上high以下のものを求める
    2分探索を用いる
    Args:
        W (list): [description]
        low (int): [description]
        high (int): [description]

    Returns:
        list: [description]
    """
    length = len(W)
    # get lowest i
    # ok = length-1
    ok = length
    ng = -1  # ngは配列の外にあるように
    while ok-ng >= 2:
        mid = (ok+ng)//2
        if W[mid] >= low:
            ok = mid
        else:
            ng = mid
    low_index = ok

    # get highest i
    #ok = 0
    ok = -1
    ng = length  # ngは配列の外にあるように
    while ng-ok >= 2:
        mid = (ok+ng)//2
        if W[mid] <= high:
            ok = mid
        else:
            ng = mid
    high_index = ok
    # いまいちっぽい点(7)
    # lowやhighがWの範囲外の時にどうすればよいのかわからない
    # 面倒なので、後でabsをとることを踏まえ[-INF, INF]にしたが、本当は空のリストを返したほうがよさそう
    if 0 <= low_index <= high_index <= length-1:
        return [W[low_index], W[high_index]]
    else:
        return [-10**23, 10**23]


def main():
    # input
    n, m = map(int, input().split())
    H = list(map(int, input().split()))
    W = list(map(int, input().split()))

    # call
    ans = solver(n, m, H, W)
    print(ans)


main()
