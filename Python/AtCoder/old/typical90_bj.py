from collections import deque


# 逆から考える
# つまり、a_i, b_iのいずれか一方が白であるとき、iを白に戻すことができる
# a_i, b_i -> iへのedgeを張る
# colは最初全てb
# a_i == i もしくは、b_i == i のとき、それを最後に使う必要がある
def main():
    node_end = int(input())
    nei_of = [[] for _ in range(node_end)]
    que = deque()
    ans = []
    col = ['b'] * node_end
    for i in range(node_end):
        a, b = map(lambda x: int(x) - 1, input().split())
        nei_of[a].append(i)
        nei_of[b].append(i)
        if a == i or b == i:
            que.append(i)
            col[i] = 'w'

    while que:
        pre = que.popleft()
        ans.append(pre+1)
        for cur in nei_of[pre]:
            if col[cur] == 'w':
                continue
            col[cur] = 'w'
            que.append(cur)

    black_list = [c for c in col if c == 'b']
    if black_list:
        print(-1)
    else:
        print(*reversed(ans))


main()
