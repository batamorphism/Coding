from collections import deque

# a_i, b_iのいずれかがwだと、iをbにできる
# 逆に見れば
# iをb -> wにできるのは、a_iかb_iがいずれwのとき
# したがって、a_i -> i, b_i -> iのedgeを張って
# wのマスから各edgeを通って全体に到達できれば、全てのボールを白に戻せる
def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    que = deque()
    col = ['b']*n
    ans = []
    for i in range(n):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(i)
        nei_of[b].append(i)
        if a == i or b == i:
            que.append(i)
            ans.append(i+1)
            col[i] = 'w'

    while que:
        pre = que.popleft()
        for cur in nei_of[pre]:
            if col[cur] == 'w':
                continue
            col[cur] = 'w'
            que.append(cur)
            ans.append(cur+1)

    # colのすべてが'w'であることを調べる
    for c in col:
        if c != 'w':
            print(-1)
            return

    print(*ans[::-1])


main()
