def main():
    n, k = map(int, input().split())
    C = list(map(int, input().split()))

    colors = {}  # 今見ている範囲の色別に、いくつのキャンディーがあるか
    ans = 0

    for i in range(n-k+1):
        if i == 0:
            # initialize colors
            for candy in range(k):
                color = C[candy]
                if color not in colors:
                    colors[C[candy]] = 0
                colors[C[candy]] += 1
        else:
            # remove_candy
            colors[C[i-1]] -= 1
            if colors[C[i-1]] == 0:
                del colors[C[i-1]]

            # add_candy
            if C[i+k-1] not in colors:
                colors[C[i+k-1]] = 0
            colors[C[i+k-1]] += 1

        ans = max(ans, len(colors))

    print(ans)


main()
