from collections import deque
from collections import Counter


def main():
    n, k = map(int, input().split())
    C = list(map(int, input().split()))

    que = deque(C[:k-1])
    cnt_of = Counter(que)
    ans = len(cnt_of)
    for c in C[k-1:]:
        que.append(c)
        cnt_of[c] += 1
        while que and not len(que) <= k:
            rm = que.popleft()
            cnt_of[rm] -= 1
            if cnt_of[rm] == 0:
                del cnt_of[rm]
        ans = max(ans, len(cnt_of))
    print(ans)


main()
