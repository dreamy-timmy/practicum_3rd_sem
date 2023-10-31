from first_lesson import tenth as ten
import numpy as np
import scipy
from first_lesson import matrix_output

print("--------------------------------------------------------------------------------------------------------")


# 1
A = ten()[0]

P, L, U = scipy.linalg.lu(A)

# 2
def second():
    print ("A:")
    matrix_output(A)


    print ("P:")
    matrix_output(P)

    print ("L:")
    matrix_output(L)

    print ("U:")
    matrix_output(U)
# second()
# 3
def third():
    determinant = 1 # так как будем получать его значение умножением

    diag_L = np.diag(L) 
    diag_U = np.diag(U)
    for i in range(len(diag_L)): # так как из условия L, U одинаковой размерности
        determinant *= diag_L[i] * diag_U[i]

    inversed_P = np.linalg.inv(P)
    determinant *= np.linalg.det(inversed_P)
    print(determinant)
# third()
# 4
from scipy import stats
def fourth():
    normal = np.round(np.random.normal(180, 10, 100))
    uniform = np.round(np.random.uniform(0, 12, 100))
    return(normal,uniform)

normal, uniform = fourth()
normal = [int(x) for x in normal]
uniform = [int(x) for x in uniform]
# print(*normal)
# print()
# print(*uniform)
# 5
def fifth():
    for sample in [normal,uniform]:
        if all(sample[i] == normal[i] for i in range(len(sample))): print("normal:")
        else: print("uniform: ")
        mean = np.mean(sample)
        mode = stats.mode(sample)
        median = np.median(sample)
        min = np.min(sample)
        max = np.max(sample)
        std = np.std(sample)
        print(f'mean = {mean}, mode = {mode}, median = {median}, min = {min}, max = {max}, standard = {round(std)}')
# fifth()
# 6
def sixth():
    print(stats.chisquare(normal))
# sixth() #значение p-value