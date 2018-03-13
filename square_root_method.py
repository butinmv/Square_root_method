eps = 1e-10    # погрешность


# Функция знака;
def sign(number):
    if number > 0:
        flag = 1
    else:
        flag = -1
    return flag


# Проверка на ноль
def checkZero(number):
    if abs(number) < eps:
        return 1
    return 0


# Проверка матрицы на симметричность
def checkSymmet(a):
    n = len(arr)
    flag = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                flag = 1
    if flag == 1:
        print("Матрица не симметрична.\nДля метода нужна симметричная матрица.")
        exit(1)


# Функция вывода матрицы на экран
def displayStartMatrix(a):
    n = len(a)
    for i in range(n):
        line = ""
        for j in range(n + 1):
            line += str("%10.5f" % a[i][j]) + "      "
            if j == n - 1:
                line += "| "
        print(line)
    print("")


# Функция вывода матрицы A на экран
def displayMatrix(a):
    n = len(a)
    for i in range(n):
        line = ""
        for j in range(n):
            line += str("%10.5f" % a[i][j]) + "      "
        print(line)
    print("")


# Перестановка строк в матрице
def swapRow(a, first_row, second_row=0):
    n = len(a)
    for i in range(n + 1):
        tmp = a[first_row][i]
        a[first_row][i] = a[second_row][i]
        a[second_row][i] = tmp


# Перестановка столбцов в матрице
def swapColumn(a, first_col, second_col=0):
    n = len(a)
    for i in range(n):
        tmp = a[i][first_col]
        a[i][first_col] = a[i][second_col]
        a[i][second_col] = tmp


# Создание матрицы A
def getMatrixA(arr):
    a = arr[:, :-1]
    return a


# Создание матрицы B
def getMatrixB(arr):
    b = arr[:, -1]
    return b


# Создание матрицы D и S
def getMatrixDS(a):
    n = len(a)

    d = np.zeros((n, n))
    s = np.zeros((n, n))

    # стартовые значения
    d[0][0] = sign(a[0][0])
    s[0][0] = math.sqrt(abs(a[0][0]))
    for j in range(1, n):
        s[0][j] = a[0][j] / s[0][0] / d[0][0]

    for i in range(1, n):
        sum = 0
        for l in range(i):
            sum += s[l][i] * s[l][i] * d[l][l]


        d[i][i] = sign(a[i][i] - sum)
        s[i][i] = math.sqrt(abs(a[i][i] - sum))

        for j in range(i + 1, n):
            sum = 0
            for l in range(n):
                sum += s[l][i] * s[l][j] * d[l][l]
            s[i][j] = (a[i][j] - sum) / s[i][i] / d[i][i]
    return d, s


# Вывод матрицы B на экран
def displayMatrixB(b):
    n = len(b)
    for i in range(n):
        print("%5.5f" % b[i], end="    ")
    print("\n")



if __name__ == "__main__":
    import numpy as np
    import copy as cp
    import math

    arr = np.loadtxt('input.txt', float)    # считываем с файла массив
    #copy_arr = cp.deepcopy(arr)

    checkSymmet(arr)

    print("Начальная матрица:")
    displayStartMatrix(arr)

    print("Матрица A:")
    a = getMatrixA(arr)
    displayMatrix(a)

    print("Матрица B:")
    b = getMatrixB(arr)
    displayMatrixB(b)

    '''
    d, s = getMatrixDS(arr)
    print("Матрица D:")
    displayMatrix(d)
    print("Матрица S:")
    displayMatrix(s)
    '''


