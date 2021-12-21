def main():
    S = input()
    acgt = 'ACGT'
    ans = 0
    cnt = 0
    for s in S:
        if s in acgt:
            # iから始まるACGT文字列の開始
            cnt += 1
        else:
            ans = max(cnt, ans)
            cnt = 0
    ans = max(cnt, ans)
    print(ans)


main()
