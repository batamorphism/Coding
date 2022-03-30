def main():
    col_end = 1000010
    col_pop = [0]*col_end

    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        col_pop[a] += 1
        col_pop[b+1] -= 1

    for col in range(1, col_end):
        col_pop[col] += col_pop[col-1]

    ans = max(col_pop)
    print(ans)


main()
