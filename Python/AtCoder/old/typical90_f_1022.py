def main():
    INF = 10**6
    n, k = map(int, input().split())
    S = input()
    DP = [[INF]*(n+1) for _ in range(26)]
    # 次の文字におけるものとして最も早い文字を貪欲に付け足す
    # 前選んだ文字の右にある文字cの中で左端のもの
    # 以降をすべて選んでk文字になる必要がある
    # 各文字cについて、i文字目より右にある文字の中で最も左にあるもののindex
    # を求めておく
    for i in range(n-1, -1, -1):
        for c in range(26):
            if ord(S[i])-ord('a') == c:
                DP[c][i] = i
            else:
                DP[c][i] = DP[c][i+1]

    ans = []
    ind = 0
    for i in range(k):
        for c in range(26):
            next_pos = DP[c][ind]
            max_possible_len = n-next_pos+i
            if max_possible_len >= k:
                ans.append(chr(c+ord('a')))
                ind = next_pos+1
                break
    print("".join(ans))


main()
