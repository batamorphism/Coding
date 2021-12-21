def main():
    r, x, y = map(int, open(0).read().split())
    dist = (x**2 + y**2)**0.5
    step = dist/r
    ans = 0
    if step == int(step):
        ans = int(step)
    elif step < 1:
        ans = int(step) + 2
    else:
        ans = int(step) + 1
    print(ans)


main()