# 尺取り法
from collections import defaultdict
from collections import deque

def main():
    n = int(input())
    S = input()
    char_list = ['o', 'x']
    cnt_of = defaultdict(int)

    def have_only(cnt_of):
        min_val = 10
        for char in char_list:
            min_val = min(min_val, cnt_of[char])
        if min_val == 0:
            return True
        return False

    ans = 0
    que = deque()
    for c in S:
        que.append(c)
        cnt_of[c] += 1
        while que and not have_only(cnt_of):
            rm = que.popleft()
            cnt_of[rm] -= 1
        # queはどっちか一方しかもっていない
        # print(que)
        ans += len(que)

    total = n*(n+1)//2
    print(total - ans)


main()
