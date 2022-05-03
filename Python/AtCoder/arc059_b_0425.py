# aaパターンか、abaパターンがあればアンバランス
def main():
    s = input()
    n = len(s)
    # aaパターン
    for i in range(n-1):
        s0 = s[i]
        s1 = s[i+1]
        if s0 == s1:
            print(i+1, i+2)
            return

    # aba パターン
    for i in range(n-2):
        s0 = s[i]
        s1 = s[i+1]
        s2 = s[i+2]
        if s0 == s2:
            print(i+1, i+3)
            return

    print(-1, -1)


main()
