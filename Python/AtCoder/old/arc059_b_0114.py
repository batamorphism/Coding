import string


# abaかaaが存在すればアンバランス
def main():
    s = '*' + input()
    # check_aa
    for c in string.ascii_lowercase:
        cc = c * 2
        for i in range(len(s)-1):
            ss = s[i:i+2]
            if cc == ss:
                print(i, i+1)
                return

    # check_aba
    for c in string.ascii_lowercase:
        for d in string.ascii_lowercase:
            cdc = c+d+c
            for i in range(len(s)-2):
                sss = s[i:i+3]
                if cdc == sss:
                    print(i, i+2)
                    return

    print(-1, -1)


main()
