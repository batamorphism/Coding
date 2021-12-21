from collections import deque
# oかxしか含まれない組み合わせ数をxとして
# 全ての組み合わせ数は、total = nH2だから
# total-xが答え


def main():
    n = int(input())
    S = input()
    cnt = {}

    que = deque()
    x = 0
    for s in S:
        que.append(s)
        cnt[s] = cnt.get(s, 0) + 1
        while que and not len(cnt) == 1:
            rm = que.popleft()
            cnt[rm] -= 1
            if cnt[rm] == 0:
                del cnt[rm]
        x += len(que)
    # nHr = (n+r-1)Cr
    total = (n+1)*n//2
    ans = total - x
    print(ans)


main()
