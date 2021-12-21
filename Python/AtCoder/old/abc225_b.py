
main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    for nei in nei_of:
        if len(nei) == n-1:
            print('Yes')
            return

    print('No')

nei_of = [[] for _ in range(n)]
main()
k