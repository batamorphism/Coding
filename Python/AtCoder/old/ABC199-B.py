def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = max(min(B)-max(A)+1, 0)
    print(ans)


main()
