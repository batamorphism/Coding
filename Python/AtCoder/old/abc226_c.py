from collections import deque


def main():
    n = int(input())
    T = []
    K = []
    A = []
    for _ in range(n):
        t, k, *a = map(int, input().split())
        k -= 1
        a = [aa-1 for aa in a]
        T.append(t)
        K.append(k)
        A.append(a)

    # 技n-1を覚えるためには、技A[n-1]を覚える必要がある
    # ただし、すでに覚えている技は覚えなおす必要はない
    color = ['w']*n  # wなら覚えていない、bなら覚えている
    que = deque()
    que.append(n-1)
    ans = 0
    while que:
        # 習得する技
        pre = que.popleft()
        ans += T[pre]
        for cur in A[pre]:
            if color[cur] == 'w':
                color[cur] = 'b'
                que.append(cur)  # 習得しなくちゃいけないやつをキューに追加

    print(ans)


main()
