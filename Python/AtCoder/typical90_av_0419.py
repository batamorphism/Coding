def main():
    n, k = map(int, input().split())
    score_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        score_list.append(b)
        score_list.append(a-b)

    score_list.sort(reverse=True)
    ans = sum(score_list[:k])
    print(ans)


main()
