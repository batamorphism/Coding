def main():
    A = list(map(int, input().split()))
    cur_val = 0
    for _ in range(3):
        cur_val = A[cur_val]
    print(cur_val)


main()
