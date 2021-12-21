from collections import deque, defaultdict


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    # しゃくとり法
    que = deque()
    cnt_of = defaultdict(int)
    ans = -1
    for a in A:
        que.append(a)
        cnt_of[a] += 1
        while que and not len(que) <= k:
            rm = que.popleft()
            cnt_of[rm] -= 1
            if cnt_of[rm] == 0:
                del cnt_of[rm]
        ans = max(ans, len(cnt_of))

    print(ans)


main()
