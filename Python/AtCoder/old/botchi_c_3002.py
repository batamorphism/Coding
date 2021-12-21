def main():
    text = input()
    # check length
    if len(text) <= 5:
        print('Invalid')
        return

    have_char = False
    have_digit = False
    for c in text:
        if c.isalpha():
            have_char = True
        else:
            have_digit = True
    if not (have_digit and have_char):
        print('Invalid')
        return

    # check 3
    for i0 in range(len(text) - 3):
        i1 = i0 + 1
        i2 = i0 + 2
        if text[i0] == text[i1] == text[i2]:
            print('Invalid')
            return

    print('Valid')


main()
