from collections import deque


def main():
    S = input()
    que = deque()
    que_cnt = {}
    ans = 0
    for s in S:
        que.append(s)
        que_cnt[s] = que_cnt.get(s, 0)+1
        while que and not check(que, que_cnt):
            rm = que.popleft()
            que_cnt[rm] -= 1
        ans = max(len(que), ans)
    print(ans)


def check(que, que_cnt):
    # queがACGTのみからなるか
    cnt = 0
    acgt = {'A', 'C', 'G', 'T'}
    for char in acgt:
        cnt += que_cnt.get(char, 0)
    return len(que) == cnt


main()
