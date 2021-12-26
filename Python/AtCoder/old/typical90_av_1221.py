# 部分点が優先
# したがって、c_i = a_i - b_iとすれば
# a_i, c_iのうち大きいものからとっていけばよい
def main():
    n, k = map(int, input().split())
    score_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        c = a-b
        score_list.append(b)
        score_list.append(c)

    score_list.sort(reverse=True)
    ans = sum(score_list[:k])
    print(ans)


main()
