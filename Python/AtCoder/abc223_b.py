def main():
    le, ri = map(int, input().split())
    le -= 1
    ri -= 1
    s = input()
    s_le = s[:le]
    s_mid = s[le:ri+1]
    s_ri = s[ri+1:]
    s_mid = s_mid[::-1]
    s_ans = s_le + s_mid + s_ri
    print(s_ans)


main()
