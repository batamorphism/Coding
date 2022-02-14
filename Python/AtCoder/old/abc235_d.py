# bfs
# 桁は増える一方であり、実はとりうるパターンは少ないことを使う
from collections import deque
from collections import defaultdict


def main():
    a, n = map(int, input().split())
    len_n = len(str(n))
    break_val = 10**len_n
    INF = float('inf')
    dist = defaultdict(lambda: INF)

    def nei_of(pre):
        # preの整数をa倍する
        ret = pre*a
        if ret <= break_val:
            yield ret
        # preをローテーションする
        if pre >= 10 and pre % 10 != 0:
            ret = pre // 10 + pre % 10 * (10**(len(str(pre))-1))
            yield ret

    dist[1] = 0
    que = deque()
    que.append(1)
    while que:
        pre = que.popleft()
        if pre == n:
            break
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur in nei_of(pre):
            if dist[cur] <= cur_d:
                continue
            dist[cur] = cur_d
            que.append(cur)

    ans = dist[n]
    if ans == INF:
        ans = -1
    print(ans)


main()
