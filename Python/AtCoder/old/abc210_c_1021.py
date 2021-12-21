from collections import deque


def main():
    n, k = map(int, input().split())
    C = list(map(int, input().split()))
    que = deque()
    cnt = {}
    ans = 0
    for c in C:
        que.append(c)
        cnt[c] = cnt.get(c, 0) + 1
        if len(que) < k:
            continue
        while que and not len(que) == k:
            rm = que.popleft()
            cnt[rm] -= 1
            if cnt[rm] == 0:
                del cnt[rm]
        ans = max(len(cnt), ans)

    print(ans)


main()
