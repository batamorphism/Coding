import heapq as hp


def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    que = []
    for le in range(N-1, -1, -1):
        ri = le + L
        # [le, ri)
        hp.heappush(que, (A[le], le))
        while not (que[0][1] < ri):
            hp.heappop(que)
        A[le] = que[0][0]

    print(*A[:N-L+1])


main()
