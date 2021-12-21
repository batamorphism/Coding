from collections import deque


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    que = deque()
    cnt_of = {}
    ans = 0
    for a in A:
        que.append(a)
        cnt_of[a] = cnt_of.get(a, 0) + 1
        while que and not len(cnt_of) <= k:
            rm = que.popleft()
            cnt_of[rm] -= 1
            if cnt_of[rm] == 0:
                del cnt_of[rm]
        ans = max(len(que), ans)
    print(ans)


main()
