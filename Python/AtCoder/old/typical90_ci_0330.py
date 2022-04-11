# 全転換距離
# 答えで二分探索
import copy

def main():
    node_end, price_max, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(node_end)]
    change_node = []
    for fr in range(node_end):
        for to in range(node_end):
            if A[fr][to] == -1:
                change_node.append((fr, to))

    def wf(A):
        dist = copy.deepcopy(A)
        for sep in range(node_end):
            for fr in range(node_end):
                for to in range(node_end):
                    dist[fr][to] = min(dist[fr][to], dist[fr][sep]+dist[sep][to])
        return dist

    def change_A(A, val):
        for fr, to in change_node:
            A[fr][to] = val

    def check(A, val, k):
        # price_max以下で到達可能な組がk個以上である
        change_A(A, val)
        dist = wf(A)
        cnt = 0
        for fr in range(node_end):
            for to in range(fr+1, node_end):
                if dist[fr][to] <= price_max:
                    cnt += 1
        return cnt >= k

    # bisect
    ok = 0
    ng = 10**9*2+1
    while ng - ok > 1:
        mid = (ok+ng)//2
        if check(A, mid, k):
            ok = mid
        else:
            ng = mid
    # xの最大値はok
    x_max = ok

    ok = 0
    ng = 10**9*2+1
    while ng - ok > 1:
        mid = (ok+ng)//2
        if check(A, mid, k+1):
            ok = mid
        else:
            ng = mid
    # xの最小値はok+1
    x_min = ok+1

    x_min = max(x_min, 1)

    ans = x_max-x_min+1
    if ans >= 10**9+1:
        ans = 'Infinity'
    print(ans)


main()
