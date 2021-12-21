from collections import deque


def main():
    n, m = map(int, map(int, input().split()))
    tubes_of = [[] for _ in range(n)]  # colに対し[tube,tube]を返す
    tube = [deque() for _ in range(m)]  # 各柱に何色のボールが入っているか
    cnt = [0]*n  # ある筒の一番上に置かれているボールのうち、色がiのもの
    que = deque()  # cnt[i] == 2となるcol
    ans = 0
    for i in range(m):
        k = int(input())
        T = list(map(int, input().split()))
        for j in range(k):
            T[j] -= 1
        tube[i] = deque(T)
        for c in tube[i]:
            tubes_of[c].append(i)

    for t in range(m):
        cnt[tube[t][0]] += 1
        if cnt[tube[t][0]] == 2:
            que.append(tube[t][0])

    while que:
        ans += 1
        col = que.popleft()
        cnt[col] = 0
        t_list = tubes_of[col]
        for t in t_list:
            tube[t].popleft()
            if len(tube[t]) != 0:
                cnt[tube[t][0]] += 1
                if cnt[tube[t][0]] == 2:
                    que.append(tube[t][0])

    if ans == n:
        print('Yes')
    else:
        print('No')


main()
