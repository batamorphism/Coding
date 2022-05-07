def main():
    n = int(input())
    S = input()

    # 考えうる答えは、000～999の1000とおり
    # それぞれが設定されうるかをO(N)で判定する
    ans = 0
    for pin_raw in range(1000):
        pin = str(pin_raw).zfill(3)
        if check(pin, S):
            ans += 1

    print(ans)


def check(pin, S):
    cur_pos = 0
    cur_char = pin[cur_pos]
    for s_i in S:
        if s_i == cur_char:
            cur_pos += 1
            if cur_pos >= 3:
                return True
            cur_char = pin[cur_pos]
    return False


main()
