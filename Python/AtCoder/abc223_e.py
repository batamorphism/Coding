def main():
    x = int(input())
    num_list = list(map(int, str(x)))
    # print(num_list)
    # 累積和
    for i in range(1, len(num_list)):
        num_list[i] += num_list[i - 1]
    # print(num_list)
    # 下から、繰り上げ処理を行う
    num_list = num_list[::-1]
    for i in range(len(num_list)):
        num = num_list[i]
        num_list[i] = 0
        j = i
        while num != 0:
            if j == len(num_list):
                num_list.append(0)
            num_list[j] += num % 10
            num //= 10
            j += 1
    # print(num_list)
    num_list = num_list[::-1]
    ans = ''.join(map(str, num_list))
    print(ans)


main()
