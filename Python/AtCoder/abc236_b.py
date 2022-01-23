def main():
    n = int(input())
    n -= 1
    cnt_of = [4]*(n+1)
    A = list(map(lambda x: int(x)-1, input().split()))
    for a in A:
        cnt_of[a] -= 1
    for i in range(n+1):
        if cnt_of[i] == 1:
            print(i+1)
            return


main()
