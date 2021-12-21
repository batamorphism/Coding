par = [i for i in range(10**5+1)]


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    par[x] = y


def same(x, y):
    return find(x) == find(y)


def main():
    node_end = int(input())
    X = []
    Y = []
    for node in range(node_end):
        x, y = map(int, input().split())
        X.append((x, node))
        Y.append((y, node))

    # x, y座標の組み合わせで最も距離が近いものから列挙する
    # x座標同士が近いもののペアは
    # x座標でソート->差を取得->差でソート
    # で得られる
    # |a-b|のedgeと|b-d|のedgeが両方あると思ってクラスカル法をすればよい
    X.sort()
    Y.sort()
    X_diff = []
    Y_diff = []
    for node in range(1, node_end):
        cost = abs(X[node][0] - X[node - 1][0])
        X_diff.append((cost, X[node][1], X[node - 1][1]))
        cost = abs(Y[node][0] - Y[node - 1][0])
        Y_diff.append((cost, Y[node][1], Y[node - 1][1]))

    XY = X_diff + Y_diff
    XY.sort()

    # クラスカル法
    ans = 0
    for cost, node1, node2 in XY:
        if same(node1, node2):
            continue
        ans += cost
        union(node1, node2)

    print(ans)


main()
