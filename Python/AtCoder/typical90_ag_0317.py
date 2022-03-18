def main():
    r_end, c_end = map(int, input().split())

    if r_end == 1:
        ans = c_end
    elif c_end == 1:
        ans = r_end
    else:
        r = (r_end+2-1)//2
        c = (c_end+2-1)//2
        ans = r*c
    print(ans)


main()
