# SIM
def main():
    n = int(input())
    T = input()
    x = 0
    y = 0
    ori = (1, 0)

    def rotate(ori):
        if ori == (1, 0):
            return (0, -1)
        if ori == (0, -1):
            return (-1, 0)
        if ori == (-1, 0):
            return (0, 1)
        else:
            return (1, 0)

    for t in T:
        if t == 'S':
            x += ori[0]
            y += ori[1]
        else:
            ori = rotate(ori)

    print(x, y)


main()
