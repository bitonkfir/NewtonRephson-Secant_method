# kfir biton : 207947698
# tamir kadosh : 206797284
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


def func(symbolic_fuction):
    return lambdify(x, symbolic_fuction, 'numpy')


def find_intervals(rangex):
    jumps = 0.1
    domains = []
    parameter = rangex[0]

    tmp = (rangex[1] - rangex[0]) / jumps
    for i in range(int(tmp)):
        domains.append([parameter, parameter + jumps])
        parameter += jumps

    return domains


def checkVariable(root, roots, eps):
    for i in roots:
        if abs(i - root) < eps:
            return False
    return True


def checkRoot(f, root, eps):
    return abs(f(root)) < eps


def secant_method(rangex, fx, x0, x1, eps, itration, printList):
    i = 0
    while abs(x1 - x0) > eps or itration == 0:
        if abs(fx(x1) - fx(x0)) < eps:
            return None
        print('     first guess: ', x0)
        print('     second guess: ', x1)
        x = x1 - fx(x1) * ((x1 - x0) / (fx(x1) - fx(x0)))
        print('     the next first guess: ', x1)
        print('     the next second guess: ', x, '\n')

        printList.append((x, i))
        i += 1
        x0 = x1
        x1 = x
        itration -= 1
    return x


def Print_roots(printList):
    for i in printList:
        print("number iteration:", i[1])
        print("Approximation:", i[0], '\n')


def all_roots(fx, eps, rangex, itration):
    j = 1
    print("***********************************************************")
    print("** Secant Formula is: X(r+1) = Xr - F(x) / F'(x) **")
    print("***********************************************************", '\n')
    roots = []
    intervals = find_intervals(rangex)
    for i in intervals:
        printList = []
        x0 = (i[0] + i[1]) / 3
        x1 = (i[0] + i[1]) / 2
        print("Interval number", j, "is: ", i, "\n")
        j += 1
        root = secant_method(rangex, fx, x0, x1, eps, itration, printList)

        if root != None:
            if (len(roots) == 0):
                if root >= rangex[0] and root <= rangex[1] and checkRoot(fx, root, eps):
                    roots.append(root)
                    print("*****************************************")
                    print("ROOT IS: [", root, ']')
                    print("*****************************************\n")
                    # Print_roots(printList)
            else:
                if root == None:
                    continue
                if (not checkVariable(root, roots, 0.1)):
                    continue
                if fx(root) == None:
                    continue
                elif root <= rangex[1] and root >= rangex[0] and checkRoot(fx, root, eps):
                    roots.append(root)
                    print("*****************************************")
                    print("ROOT IS: [", root, ']')
                    print("*****************************************\n")
                    # Print_roots(printList)
    if len(roots) == 0:
        return None
    roots.sort()
    print("The root list is: ", roots)
    return roots


def plot_it(start, end, function, methodName):
    # Data for plotting
    t = np.arange(start, end, 0.01)
    s = function(t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='X', ylabel='Y',
           title=methodName)
    ax.grid()

    fig.savefig("test.png")
    plt.show()


if __name__ == '__main__':
    x = Symbol('x')
    epsilon = 0.0001
    fx = input("enter an polynom:(example:x**3-3*(x**2)):")
    Start_Domain = float(input("enter the domain start:"))
    End_Domain = float(input("enter the domain end:"))
    assginment_func = func(fx)
    fx = assginment_func
    all_roots(fx,epsilon,[Start_Domain,End_Domain],100)
    plot_it(0, 1, fx, "Secant")