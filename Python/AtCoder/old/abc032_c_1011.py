from collections import deque


def main():
    n, k = map(int, input().split())
    Arr = [int(input()) for _ in range(n)]
    if 0 in Arr:
        print(n)
        return
    # しゃくとり
    # queを使った実装。que自身が尺取り虫
    que = deque()
    ans = 0
    prod = 1
    for a in Arr:
        que.append(a)
        prod *= a
        while que and not prod <= k:
            rm = que.popleft()
            prod //= rm
        ans = max(len(que), ans)

    print(ans)


main()
