def main():
    r_end, c_end = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r_end)]
    B = list(map(list, zip(*A)))
    for b in B:
        print(*b)


main()
