from collections import deque


def main():
    n = int(input())
    S = input()
    # 全組み合わせ数は、nH2 = (n+2-1)C2
    all = (n+1)*n//2
    # oかxしか含まれない部分を求める
    comp = 0
    que = deque()
    cnt_of = {'o': 0, 'x': 0}
    for s in S:
        que.append(s)
        cnt_of[s] += 1
        while que and not (cnt_of['o'] == 0 or cnt_of['x'] == 0):
            rm = que.popleft()
            cnt_of[rm] -= 1
        comp += len(que)
    print(all-comp)


main()
