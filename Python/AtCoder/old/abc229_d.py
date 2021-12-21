from collections import deque


def main():
    # .を1、Xを0とする
    # しゃくとり法
    # 1がk個含まれている区間の長さの最大値を求める
    # ただし、全体でも1がk個未満しかないときは、全体とする
    S = input()
    k = int(input())
    A = []
    for s in S:
        if s == '.':
            A.append(1)
        else:
            A.append(0)

    if sum(A) < k:
        print(len(A))
        return

    que = deque()
    cnt = 0
    ans = -1
    for a in A:
        que.append(a)
        cnt += a
        while que and not (cnt <= k):
            rm = que.popleft()
            cnt -= rm
        # print(que)
        ans = max(ans, len(que))

    print(ans)


main()
