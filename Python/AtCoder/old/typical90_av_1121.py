def main():
    n, k = map(int, input().split())
    score_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        score_list.append(b)
        score_list.append(a-b)

    score_list.sort(reverse=True)
    get_score_list = score_list[:k]
    ans = sum(get_score_list)
    print(ans)


main()
