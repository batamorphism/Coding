def main():
    k, t = map(int, map(int, input().split()))
    A = list(map(int, input().split()))
    # Aのうちもっとも頻度が多いものを均等に配置し
    # それ以外をその隙間に埋めていく
    cnt_of = [(cnt, i) for i, cnt in enumerate(A)]
    cnt_of.sort(reverse=True)
    max_cnt, max_a = cnt_of[0]
    other_cnt = k-max_cnt
    ans = max(max_cnt-other_cnt-1, 0)
    print(ans)


main()
