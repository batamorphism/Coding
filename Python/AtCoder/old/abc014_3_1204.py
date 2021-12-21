# imos
def main():
    n = int(input())
    AB = []
    for _ in range(n):
        a, b = map(int, input().split())
        # 累積和は1-origin
        a += 1
        b += 1
        AB.append((a, b))

    colors = [0] * (1000000+10)
    for a, b in AB:
        colors[a] += 1
        colors[b+1] -= 1

    for i in range(1, len(colors)):
        colors[i] += colors[i-1]

    ans = max(colors)
    print(ans)


main()
