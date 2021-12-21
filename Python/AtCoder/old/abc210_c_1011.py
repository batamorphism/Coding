from collections import deque


def main():
    n, k = map(int, input().split())
    candy_list = list(map(int, input().split()))
    que = deque()
    cnt = {}
    ans = 0
    for ad in candy_list:
        que.append(ad)
        cnt[ad] = cnt.get(ad, 0) + 1
        while que and not len(que) <= k:
            rm = que.popleft()
            cnt[rm] -= 1
            if cnt[rm] == 0:
                del cnt[rm]
        ans = max(len(cnt), ans)

    print(ans)


main()
