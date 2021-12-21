def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    solver(points, n)


def solver(points: list, n):
    """solver
    n<=10**2
    n個の点の相異なる3点で、同一線上にあるものがあるか
    O(n**3)は10**6なので間に合う
    Args:
        points (list): [description]
    """
    is_no = True
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if is_on_same_line(points[i], points[j], points[k]):
                    is_no = False
    if is_no:
        print('No')
    else:
        print('Yes')


def is_on_same_line(point1: list, point2: list, point3: list) -> bool:
    """
    同直線上にあるということは、
    ある実数rが存在し、point1+(point2-point1)*r = point3
    すなわち、
    r = (point3-point1)/(point2-point1)
    ただし、point1とpoint2が同じだった場合は、point1とpoint3が同じ場合はrは任意
    違う場合はFalseを返す
    これを、x,yそれぞれに対して行い作成した2つのrが一致することを確認する
    """
    rx = 0
    ry = 0
    # dividend by zero
    if (point2[0]-point1[0]) == 0:
        if point1[0] == point3[0]:
            return True
        else:
            return False
    else:
        rx = (point3[0]-point1[0])/(point2[0]-point1[0])

    if (point2[1]-point1[1]) == 0:
        if point1[1] == point3[1]:
            return True
        else:
            return False
    else:
        ry = (point3[1]-point1[1])/(point2[1]-point1[1])

    if abs(rx-ry) <= 1e-8:
        return True
    else:
        return False


main()