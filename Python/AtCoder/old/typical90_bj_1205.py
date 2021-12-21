from collections import deque
# 後ろから考える
# 最初、ボールはすべて黒いとする
# AかBがiであるか、AかBのどちらか一方が白の時に、ボールiを白に変えることができる


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    que = deque()
    for i in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        # aかbが白であった場合、iを操作できる
        nei_of[a].append(i)
        nei_of[b].append(i)
        if a == i or b == i:
            que.append(i)

    col = ['b']*n
    ans = deque()
    while que:
        pre = que.popleft()
        if col[pre] == 'w':
            continue
        ans.appendleft(pre)
        col[pre] = 'w'
        for cur in nei_of[pre]:
            if col[cur] == 'b':
                # curが次にできる操作
                que.append(cur)

    if len(ans) != n:
        print(-1)
        return

    for a in ans:
        print(a+1)


main()
