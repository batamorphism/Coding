# cnt_A[x] = A mod 46 が xとなる個数
# 46**3通り試せばよい
def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    cnt_A = [0] * 46
    cnt_B = [0] * 46
    cnt_C = [0] * 46
    for arr, cnt in zip([A, B, C], [cnt_A, cnt_B, cnt_C]):
        set_mod46(arr)
        set_cnt(arr, cnt)

    ans = 0
    for a in range(46):
        for b in range(46):
            for c in range(46):
                if (a+b+c) % 46 == 0:
                    ans += cnt_A[a] * cnt_B[b] * cnt_C[c]

    print(ans)


def set_mod46(A):
    for i in range(len(A)):
        A[i] %= 46


def set_cnt(A, cnt_A):
    for a in A:
        cnt_A[a] += 1


main()
