def main():
    n = int(input())
    P = list(map(int, input().split()))
    for i in range(n):
        P[i] -= 1

    Q = [0]*n

    for i in range(n):
        Q[P[i]] = i+1

    for q in Q:
        print(q)


main()