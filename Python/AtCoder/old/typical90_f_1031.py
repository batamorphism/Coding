INF = 10**9


def main():
    n, k = map(int, input().split())
    S = input()
    # 辞書順は前から貪欲法
    atoz = [chr(i) for i in range(ord('a'), ord('z')+1)]
    search = {}  # 次にその文字が出てくるタイミング ('a', 1)をkeyにしたら、1以降で初めてaが出てくる場所
    for i in range(n-1, -1, -1):
        c = S[i]
        for char in atoz:
            if char == c:
                search[(char, i)] = i
            else:
                search[(char, i)] = search.get((char, i+1), INF)

    ans = []
    i = 0
    while i < n:
        for char in atoz:
            char_i = search[(char, i)]
            # char以降の文字数がk-len(ans)以下だったら不採用
            if n-char_i < k-len(ans):
                continue
            ans.append(char)
            i = char_i+1
            if len(ans) >= k:
                print(''.join(ans))
                return
            break
    print(ans)


main()
