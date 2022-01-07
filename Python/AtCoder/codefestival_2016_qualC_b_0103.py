# 一番多いケーキを並べて
# その間にほかのケーキを挟んでいく
def main():
    k, t = map(int, input().split())
    A = list(map(int, input().split()))
    max_a = max(A)
    oth_a = sum(A) - max_a

    if max_a-1 <= oth_a:
        print(0)
        return

    ans = (max_a-1) - oth_a
    print(ans)


main()
