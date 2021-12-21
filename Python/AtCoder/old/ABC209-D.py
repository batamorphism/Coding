import queue


def solver(n: int, q: int, edge: list, query: list):
    """solver
    n個のnodeとn-1本のedgeからなる木
    各edgeの長さは同じ
    q個のqueryが与えられる
    queryでは、t君は街q[0]に、a君はq[1]にいる。
    それぞれ街q[1]、q[0]を目指して移動するとき、二人が
    街で出会うか道路上で出会うか判定せよ

    Args:
        n (int): [description]
        q (int): [description]
        edge (list): [description]
        query (list): [description]
    """
    """
    q[0]からq[1]への最短距離が2の倍数かどうかを判定すればよい
    これは、node=0から各nodeへの距離distを計算し
    dist[q[0]]+dist[q[1]]が2の倍数かどうかを判定すればよい
    """
    # 0からの距離dist[node]をbfsで計算する
    dist = [-1]*n
    color = ['w']*n
    # 隣接リストを生成する
    to = [[] for _ in range(n)]
    for e in edge:
        to[e[0]].append(e[1])
        to[e[1]].append(e[0])
    # bfs
    Que = queue.Queue()
    Que.put(0)
    color[0] = 'g'
    dist[0] = 0
    while not Que.empty():
        u = Que.get()
        for v in to[u]:
            if color[v] == 'w':
                color[v] = 'g'
                dist[v] = dist[u]+1
                Que.put(v)
        color[u] = 'b'

    del Que, color, to

    # solve
    for q in query:
        is_town = (dist[q[0]]+dist[q[1]]) % 2 == 0
        if is_town:
            print('Town')
        else:
            print('Road')


def main():
    # input
    n, q = map(int, input().split())

    edge = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        edge.append([a-1, b-1])

    query = []
    for _ in range(q):
        c, d = map(int, input().split())
        query.append([c-1, d-1])

    # solve
    solver(n, q, edge, query)


main()
