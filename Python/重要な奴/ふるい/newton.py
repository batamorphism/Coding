
import traceback
import matplotlib.pyplot as plt
# import csv


def Main():
    d =[0,1,4,9,16]
    plt.plot(d)
    plt.show()


def newton(solv_f, x0):
    eps = 1e-10
    error = 1e-10
    solv_df = (solv_f(x0 + eps) - solv_f(x0 - eps))/(2 * eps)
    x1 = x0 - solv_f(x0)/solv_df
    if(abs(x1-x0) <= error):
        return x1
    return newton(solv_f, x1)


def my_func(x):
    return x ** 2 + x - 10


def my_func2(a1):
    return A1(a1) - a1


def A0():
    return 1


def A1(a1):
    return A0() + I0(a1) - W(a1)


def I0(a1):
    return ((A0() + a1)*0.01)/(2+0.01)


def W(a1):
    return -((A0() + a1)*0.05)/(2+0.05)


if __name__ == "main":
    Main()
else:
    Main()
