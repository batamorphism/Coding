def main():
    S = [input() for _ in range(3)]
    T = input()
    ans = []

    for i in range(len(T)):
        j = int(T[i])-1
        ans.append(S[j])

    ans2 = "".join(ans)

    print(ans2)


main()
