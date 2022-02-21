import random


def operation(grid, pet_list, human_list):
    ret = []
    for human in human_list:
        ori = random.randint(0, 3)
        UDLR = ['U', 'D', 'L', 'R']
        ret.append(UDLR[ori])
    return ''.join(ret)


def main():
    pet_end = int(input())
    pet_list = []
    for _ in range(pet_end):
        x, y, t = map(int, input().split())
        x -= 1
        y -= 1
        pet_list.append([x, y, t])

    human_end = int(input())
    human_list = []
    for _ in range(human_end):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        human_list.append([x, y, -1])

    grid = [[0]*30 for _ in range(30)]

    for _ in range(300):
        print(operation(grid, pet_list, human_list))
        pet_strategy = list(input().split())
        for pet in range(pet_end):
            strategy = pet_strategy[pet]
            if strategy == 'U':
                pet_list[pet][0] -= 1
            elif strategy == 'D':
                pet_list[pet][0] += 1
            elif strategy == 'L':
                pet_list[pet][1] -= 1
            elif strategy == 'R':
                pet_list[pet][1] += 1


main()
