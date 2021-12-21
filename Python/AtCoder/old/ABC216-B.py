def main():
    n = int(input())
    S = []
    T = []
    for _ in range(n):
        s, t = input().split()
        S.append(s)
        T.append(t)

    ans = 'No'
    for i in range(n):
        for j in range(i+1, n):
            if (S[i] == S[j]) and (T[i] == T[j]):
                ans = 'Yes'
                break

    print(ans)


main()