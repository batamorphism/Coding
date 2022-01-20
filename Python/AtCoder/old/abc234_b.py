from itertools import product


def main():
    n = int(input())
    point_list = [tuple(map(int, input().split())) for _ in range(n)]

    ans = -float('inf')
    for p1, p2 in product(point_list, repeat=2):
        x = p1[0] - p2[0]
        y = p1[1] - p2[1]
        val = (x**2 + y**2)**0.5
        ans = max(ans, val)

    print(ans)


main()
