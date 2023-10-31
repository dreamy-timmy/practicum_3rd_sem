#1

import numpy as np
from random import randint

def float_to_integer_in_array(a):
    return [int(x) if x.is_integer() else round(x,2) for x in a]


def matrix_output(matrix):
    print('\n'.join('\t'.join(map(str, float_to_integer_in_array(row))) for row in matrix))



def first():
    my_array = np.arange(10, 70, 2)
    return my_array
# print(*first())

#
def second():
    my_array = first()
    a = my_array.reshape(6, 5)
    a = a.transpose()
    return a
# matrix_output(second())

def third():
    a = second()
    a = np.multiply(a, 2.5)
    rand = randint(0, 4)
    a[rand] = np.subtract(a[rand], 5)
    a = a.astype("int")
    return a

# matrix_output(third())



def fourth():
    b = np.random.rand(6, 3) * 10
    return b

# matrix_output(fourth())

def fifth():
    addable = third()
    a = np.zeros((1, 6))
    for i in range(addable.shape[0]):
        a += addable[i]

    b = np.zeros((1,5))
    transposen = addable.transpose()
    for i in range(transposen.shape[0]):
        b += transposen[i]

    print(f'the shape of a = {a.shape}')
    print(f'the shape of b = {b.shape}')

# fifth()

#
def sixth():
    A = second()
    B = fourth()
    C = np.matmul(A,B)
    return C
# matrix_output(sixth())

def seventh():
    A = second()
    A = np.delete(A, 2, 1)
    B = fourth()
    B1 = np.c_[B, np.random.randint(10, 20, (np.shape(B)[0], 1)), np.random.randint(10, 20, (np.shape(B)[0], 1)), np.random.randint(10, 20, (np.shape(B)[0], 1))]
    print(f'the changed shape of a = {A.shape}')
    print(f'the changed shape of b = {B1.shape}')
    return A,B1
# seventh()

def eighth():
    A, B = seventh()
    detA, detB = np.linalg.det(A), np.linalg.det(B)
    if detA != 0:
        invA = np.linalg.inv(A)
        matrix_output(invA)
    print()
    if detB != 0:
        invB = np.linalg.inv(B)
        matrix_output(invB)

# eighth()

def nineth():
    A, B = seventh()
    A6 = np.linalg.matrix_power(A,6)
    B14 = np.linalg.matrix_power(B, 14)
    matrix_output(A6)
    print()
    matrix_output(B14)
# nineth()

def tenth(): # 4 вариант
    A = np.array([[2.3, 0, -3.4, -12], [2.6, 8.4, -9, 3], [1.3, 4.5, -17, 2], [1.8, 0, 15, 16]])
    V = np.array([14, 0.4, -3.6, 17.4])
    solution = np.linalg.solve(A,V)
    return A,solution
    #for i in range(len(solution)): print(f'x{i+1} = {solution[i]}')

# solution = tenth()[1]
# print(solution)
# for i in range(len(solution)): print(f'x{i+1} = {solution[i]}')
