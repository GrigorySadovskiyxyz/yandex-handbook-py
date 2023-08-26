import numpy as np

def snake(MM, NN, direction='H'):
    # Создаем пустую матрицу
    matrix = np.zeros((NN, MM), dtype=np.int16)
    
    # Если направление горизонтальное
    if direction == 'H':
        num = 1
        for i in range(NN):
            if i % 2 == 0:  # Если четная строка
                for j in range(MM):
                    matrix[i][j] = num
                    num += 1
            else:  # Если нечетная строка
                for j in range(MM-1, -1, -1):
                    matrix[i][j] = num
                    num += 1
    # Если направление вертикальное
    elif direction == 'V':
        num = 1
        for j in range(MM):
            if j % 2 == 0:  # Если четный столбец
                for i in range(NN):
                    matrix[i][j] = num
                    num += 1
            else:  # Если нечетный столбец
                for i in range(NN-1, -1, -1):
                    matrix[i][j] = num
                    num += 1
    return matrix


print(snake(5, 3))
