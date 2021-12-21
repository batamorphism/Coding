def main():
    n = int(input())
    S = input()
    ans = 0
    for pin_int in range(1000):
        pin = str(pin_int).zfill(3)
        if check(pin, S):
            ans += 1
    print(ans)


def check(pin: str, S: str):
    pin_ind = 2
    for s in S:
        if s == pin[pin_ind]:
            pin_ind -= 1
            if pin_ind < 0:
                return True
    return False


main()
