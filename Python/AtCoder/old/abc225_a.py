def main():
    S = input()
    cnt_of = {}
    for s in S:
        cnt_of[s] = cnt_of.get(s, 0) + 1
    if len(cnt_of) == 3:
        print(1)
    elif len(cnt_of) == 2:
        print(3)
    else:
        print(6)

main()
