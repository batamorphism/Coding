# n枚の皿に、A[i]個のミカンが置いてある
# l番目からr番目までの皿からx個ずつ取る

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for left in range(n):
        x = 10**24
        for right in range(left, n):
            if x > A[right]:
                x = A[right]
            pre_ans = x*(right-left+1)
            if ans < pre_ans:
                ans = pre_ans

    print(ans)


main()