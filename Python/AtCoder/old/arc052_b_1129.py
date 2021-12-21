import math
PI = math.pi


def main():
    n, q = map(int, input().split())
    tri_list = []
    for _ in range(n):
        x, r, h = map(int, input().split())
        tri_list.append((x, r, h))

    query_list = []
    for _ in range(q):
        a, b = map(int, input().split())
        query_list.append((a, b))

    for lo, hi in query_list:
        ans = 0
        for tri in tri_list:
            ans += calc_area(tri, lo, hi)
        print(ans)


def calc_area(tri, lo, hi):
    x, r, h = tri
    x_lo = x
    x_hi = x + h
    lo = max(lo, x_lo)
    hi = min(hi, x_hi)
    

main()
