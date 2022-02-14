def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        # s の各bitについて、見ていく
        bit_end = max(len(bin(s)[2:]), len(bin(a)[2:]))
        bxyasn_list_list = []
        for bit in range(bit_end):
            bxyasn_list = []
            a_bit = a >> bit & 1
            s_bit = s >> bit & 1
            if a_bit == s_bit == 0:
                bxyasn = [0, 0, 0, 0, 0, 0]
                bxyasn_list.append(bxyasn)
                bxyasn = [1, 1, 0, 0, 0, 1]
                bxyasn_list.append(bxyasn)
                bxyasn = [1, 0, 1, 0, 0, 1]
                bxyasn_list.append(bxyasn)
            elif a_bit == 0 and s_bit == 1:
                bxyasn = [1, 0, 0, 0, 1, 0]
                bxyasn_list.append(bxyasn)
                bxyasn = [0, 1, 0, 0, 1, 0]
                bxyasn_list.append(bxyasn)
                bxyasn = [0, 0, 1, 0, 1, 0]
                bxyasn_list.append(bxyasn)
            elif a_bit == 1 and s_bit == 0:
                bxyasn = [0, 1, 1, 1, 0, 1]
                bxyasn_list.append(bxyasn)
            else:
                bxyasn = [1, 1, 1, 1, 1, 1]
                bxyasn_list.append(bxyasn)
            bxyasn_list_list.append(bxyasn_list)

        bef_type = [0]  # 前の繰り上がりとしてあり得るもの
        is_yes = True
        for i, bxyasn_list in enumerate(bxyasn_list_list):
            is_last = False
            if i + 1 == len(bxyasn_list_list):
                is_last = True
            aft_type = []  # 後の繰り上がりとしてあり得るもの
            for b, _, _, _, _, n in bxyasn_list:
                if b in bef_type:
                    if n not in aft_type:
                        aft_type.append(n)
            if not aft_type:
                is_yes = False
                break
            if is_last and (0 not in aft_type):
                is_yes = False
                break
            bef_type = aft_type[:]
        if is_yes:
            print('Yes')
        else:
            print('No')



main()
