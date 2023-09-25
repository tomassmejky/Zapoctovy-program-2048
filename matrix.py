import random
import data as d

def rotate_matrix_counter_clockwise(matrix, score):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)], score
def rotate_matrix_180(matrix, score):
    return [[matrix[i][j] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)], score
def rotate_matrix_clockwise(matrix, score):
    return [list(reversed(col)) for col in zip(*matrix)], score



def generate_tile(matrix):
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    while matrix[a][b] != 0:
        a = random.randint(0, 3)
        b = random.randint(0, 3)
    matrix[a][b] = 2 if random.uniform(0, 100) < 90 else 4
    return matrix

def new_game():
    matrix = []
    for i in range(4):
        matrix.append([0]*4)
    generate_tile(matrix)
    generate_tile(matrix)
    return matrix

def compress(matrix, score):
    for i in range(3):
        for j in range(4):
            if matrix[i][j] == 0 and matrix[i+1][j] != 0:
                for k in reversed(range(i+1)):
                    if matrix[k][j] == 0 and matrix[k+1][j] != 0:
                        matrix[k][j], matrix[k+1][j] = matrix[k+1][j], matrix[k][j]
    return matrix, score

def addition(matrix, score):
    checkpoint = [True]*4
    for i in range(3):
        for j in range(4):
            if checkpoint[j] and matrix[0][j] == matrix[1][j] and matrix[2][j] == matrix[3][j]:
                score += matrix[0][j]*2 + matrix[2][j]*2
                matrix[0][j], matrix[1][j] = matrix[0][j]*2, matrix[2][j]*2
                matrix[2][j], matrix[3][j] = 0, 0
                checkpoint[j] = False
            
            if checkpoint[j] and matrix[i][j] == matrix[i+1][j]:
                score += matrix[i][j]*2
                matrix[i][j], matrix[i+1][j] = matrix[i][j]*2, 0
                checkpoint[j] = False
    return matrix, score

def win(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return True
    return False

def loss(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i+1][j] or matrix[i][j+1] == matrix[i][j]:
                return False
    for k in range(3):  
        if matrix[3][k] == matrix[3][k+1]:
            return False
    for j in range(3): 
        if matrix[j][3] == matrix[j+1][3]:
            return False
    return True

def swipe_up(matrix, score):
    return compress(*addition(*compress(matrix, score)))

def swipe_down(matrix, score):
    return rotate_matrix_180(*compress(*addition(*compress(*rotate_matrix_180(matrix, score)))))

def swipe_left(matrix, score):
    return rotate_matrix_counter_clockwise(*compress(*addition(*compress(*rotate_matrix_clockwise(matrix, score)))))

def swipe_right(matrix, score):
    return rotate_matrix_clockwise(*compress(*addition(*compress(*rotate_matrix_counter_clockwise(matrix, score)))))
