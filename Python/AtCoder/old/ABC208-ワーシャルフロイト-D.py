def solver(n: int, path_list: list):
    """n個のnodeとm個のpathがある
    pathは[0]から[1]への一方通行で[2]分かかる

    f(s,t,k)を次で定義する
    都市sを出発して都市tに到着するまでの最短時間を計算せよ
    ただし、通ってよい都市は番号がk以下の都市のみとする（始点と終点は除く）
    ただし、都市tに到着できない場合およびs=tの場合は0とする

    ここで、全てのs,t,kの組み合わせに対して、f(s,t,k)の総和を求めよ
    400**3=64,000,000なので、O(1)で計算しない限り全探索は無理
    全ての頂点の組(s,t)について、最短経路を求めるにはO(n^3)‥ダメっぽい

    ワーシャルフロイト法
    dist[k][i][j]を、0,...,kまでを経由する頂点i,jの最短コストとする
    dist[-1][i][j]は、path[i][j]のみが入る
    pathがなければ、infとする
    dist[-1][i][i]は0とする
    
    次に、k=0,...,n-1について、dist[k-1]に基づいてdist[k]を求める
    dist[k][i][j] = min(dist[k-1][i][j], mindist[k-1][i][k]+dist[k-1][k][j])となる
    つまり、k=0の時は
    dist[k][i][j] = min(dist[k-1][i][j], mindist[k-1][i][k]+dist[k-1][k][j])となる
    
    
    Args:
        path_list (list): [description]
    """
    INF = 10**10
    # dist = [[[INF]*n for _ in range(n)] for _ in range(n+1)]
    dist = [[INF]*n for _ in range(n)]
    # init

    for i in range(n):
        dist[i][i] = 0
    for path in path_list:
        dist[path[0]][path[1]] = path[2]

    ans = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                if dist[i][j] != INF:
                    ans += dist[i][j]

    print(ans)


def main():
    # input
    n, m = map(int, input().split())
    path_list = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        path_list.append([a-1, b-1, c])
    solver(n, path_list)


main()