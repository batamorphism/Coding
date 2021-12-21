# スライド最小値
from heapq import heappush, heappop


def main():
    n_end, k = map(int, input().split())
    A = list(map(int, input().split()))
    que = []

    for le in range(n_end-1, -1, -1):
        # [le, ri]
        ri = le + k - 1
        heappush(que, (A[le], le))
        while que[0][1] > ri:
            heappop(que)
        A[le] = que[0][0]

    B = A[:n_end-k+1]
    print(*B)


main()
