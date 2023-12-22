import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import third_lesson
import second_lesson
print("--------------------------------------------------------------------------------------------------------")

def first():
    f = lambda x: 2/(np.sin(x) + 4)
    a = 3 
    b = 6
    n = 30 # раобъём отрезок на 30 частей
    length = b-a
    step = length/n


    points = []
    for x in range(a*10,b*10+1,int(step*10)): 
        x /= 10 # поскольку умножили на 10, чтобы step был int
        points.append(x)

    f_values = [round(f(x),3) for x in points]
    return (points, f_values)
f = first()
points, f_values = f[0], f[1]

# print(points)
# print(values)

# 2
def second():
    plt.plot(points, f_values, linewidth = 3.0, label='function line')
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.title("function graphics", fontsize=18)
    plt.legend()
    plt.show()
# second()

# 3

def third():
    plt.plot(points, f_values, linewidth = 3.0, linestyle = ':', marker = "*", label='function line', color = "r")
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.title("function graphics", fontsize=18)

    plt.grid ( visible=True, which='both', color='b', linewidth=1.5 )
    plt.show() 
# third()

def fourth():
    uniform = third_lesson.uniform
    normal = third_lesson.normal
    plt.hist(uniform, rwidth=0.25, color='g')
    
    plt.title("Uniform sample")
    plt.show()

    plt.hist(normal, color='y')
    plt.title("Normal sample")
    plt.show()
# fourth()

def fifth():
    int_uniform = np.round(np.random.randint(1, 5, 50))
    unique_counts = np.unique(int_uniform, return_counts=True)
    print(unique_counts)

    plt.pie(unique_counts[1], labels=unique_counts[0], colors=['#b2de21','#4c0d57','#574b0d','#0d5750'])
    plt.show()
    plt.bar(unique_counts[0], unique_counts[1], color=['#b2de21','#4c0d57','#574b0d','#0d5750'] ) 
    plt.show()
    
# fifth()
import mpl_toolkits.mplot3d.axes3d as mpl3d
def sixth():
    f = lambda x1,x2: second_lesson.fifth_f(x1,x2)

    a = 0
    b = 30
    n = 10  # раобьём отрезок на 10 частей
    length = b-a
    step = length//n

    points = []
    for x in range(a,b+1,step): 
        points.append(x)

    f_values = [round(f(x,x),3) for x in points ]
    
    fig = plt.figure(figsize=(7, 4))

    ax = fig.add_subplot(111, projection='3d')

    ax.plot(points, points, f_values, color = '#b2de21')
    plt.show()

# sixth()

def seventh():
    # fig, axs = plt.subplots(ncols=2, nrows=2,  figsize=(12, 10), layout="constrained",)
    # plt.suptitle()
    fig = plt.figure(figsize=(12, 10))
    fig.suptitle("All four graphs on a same figure",  fontsize=18)
    # график 1
    fig.add_subplot(2, 2, 1)
    f = first()
    points, f_values = f[0], f[1]
    plt.plot(points, f_values, linewidth = 3.0, label='function line')
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.title("function graphics", fontsize=18)
    plt.legend()

    # график 2
    fig.add_subplot(2, 2, 2)
    plt.plot(points, f_values, linewidth = 3.0, linestyle = ':', marker = "*", label='function line', color = "r")
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.title("function graphics", fontsize=18)

    plt.grid (visible=True, which='both', color='b', linewidth=1.5 )

    # график 3
    fig.add_subplot(2, 2, 3)
    int_uniform = np.round(np.random.randint(1, 5, 50))
    unique_counts = np.unique(int_uniform, return_counts=True)

    plt.pie(unique_counts[1], labels=unique_counts[0], colors=['#b2de21','#4c0d57','#574b0d','#0d5750'])

    # график 4
    f = lambda x1,x2: second_lesson.fifth_f(x1,x2)
    a = 0
    b = 30
    n = 10  # раобьём отрезок на 10 частей
    length = b-a
    step = length//n
    points = []
    for x in range(a,b+1,step): points.append(x)

    f_values = [round(f(x,x),3) for x in points ]
    

    ax = fig.add_subplot(2, 2, 4, projection='3d')

    ax.plot(points, points, f_values, color = '#b2de21')

    fig.axes[0].set_facecolor('violet')
    plt.show()

# seventh()

def eighth():
    ...

    