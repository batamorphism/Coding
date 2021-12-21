def main():
    n = int(input())
    ABT = []
    total_time = 0
    for _ in range(n):
        a, b = map(int, input().split())
        t = a/b
        total_time += t
        ABT.append((a, b, t))
    ans_time = total_time / 2  # この時刻経過時点で燃え尽きる
    ans = 0
    time = 0
    for a, b, t in ABT:
        if time+t >= ans_time:
            # 全て燃え尽きた
            ans += b*(ans_time-time)
            break
        ans += a
        time += t

    print(ans)


main()
