# Проверка матрицы на симметричность
def checkSymmet(arr):
    n = len(arr)
    flag = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                flag = 1
    if flag == 1:
        print("Матрица не симметрична.\nДля метода нужна симметричная матрица.")


if __name__ == "__main__":
    import numpy as np
    arr = np.loadtxt('input.txt', float) # считываем с файла массив
    checkSymmet(arr)

