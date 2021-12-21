from collections import deque


def main():
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]

    que = deque()
    for query in query_list:
        t, x = query
        if t == 1:
            que.appendleft(x)
        elif t == 2:
            que.append(x)
        else:
            print(que[x-1])


main()
