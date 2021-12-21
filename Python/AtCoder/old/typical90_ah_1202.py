from collections import deque
from collections import Counter


# しゃくとり法
def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    que = deque()
    cnt_of = Counter()
    ans = -1
    for a in A:
        que.append(a)
        cnt_of[a] += 1
        while que and not (len(cnt_of) <= k):
            rm = que.popleft()
            cnt_of[rm] -= 1
            if cnt_of[rm] == 0:
                del cnt_of[rm]
        ans = max(ans, len(que))

    print(ans)


main()
