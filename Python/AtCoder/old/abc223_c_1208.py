# 両端から考える
def main():
    n = int(input())
    item_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        time = a/b
        item_list.append((a, b, time))

    time_sum = 0
    for _, _, time in item_list:
        time_sum += time

    ans_time = time_sum / 2
    # ans_time秒後にどこが燃えているか求める
    ans = 0
    for a, b, time in item_list:
        if time < ans_time:
            ans += a
            ans_time -= time
        else:
            ans += b*ans_time
            ans_time = 0
            break

    print(ans)


main()
