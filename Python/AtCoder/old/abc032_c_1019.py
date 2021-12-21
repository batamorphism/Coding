from collections import deque


def main():
    n, k = map(int, input().split())
    S = [int(input()) for _ in range(n)]
    prod = 1
    que = deque()
    ans = 0
    for s in S:
        if s == 0:
            ans = n
            break
        que.append(s)
        prod *= s
        while que and not prod <= k:
            rm = que.popleft()
            prod //= rm
        ans = max(len(que), ans)
    print(ans)


main()
