# xとy独立
def main():
    n = int(input())
    x_list = []
    y_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    # 中央値が答え
    x_list.sort()
    y_list.sort()
    x_val = solve(x_list, n)
    y_val = solve(y_list, n)
    ans = x_val+y_val
    print(ans)


def solve(x_list, n):
    mid = n//2
    ans = 0
    mid_x = x_list[mid]
    for x in x_list:
        ans += abs(x-mid_x)
    return ans


main()
