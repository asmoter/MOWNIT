import random
import matplotlib.pyplot as plt

color = 'black'

X = [0]
Y = [0]

f_1_f = [0, 0, 0, 0, 0.16, 0]
f_2_f = [0.85, 0.04, 0, -0.04, 0.85, 1.6]
f_3_f = [0.2, -0.26, 0, 0.23, 0.22, 1.6]
f_4_f = [-0.15, 0.28, 0, 0.26, 0.24, 0.44]

f_1_t = [0.05, 0, 0, 0, 0.6, 0]
f_2_t = [0.05, 0, 0, 0, -0.5, 1]
f_3_t = [0.46, -0.321, 0, 0.386, 0.383, 0.6]
f_4_t = [0.47, -0.154, 0, 0.171, 0.423, 1.1]
f_5_t = [0.433, 0.275, 0, -0.25, 0.476, 0.16]
f_6_t = [0.421, 0.257, 0, -0.353, 0.306, 0.7]

f_1_t2 = [0.01, 0, 0, 0, 0.45, 0]
f_2_t2 = [-0.01, 0, 0, 0, -0.45, 0.4]
f_3_t2 = [0.42, -0.42, 0, 0.42, 0.42, 0.4]
f_4_t2 = [0.42, 0.42, 0, -0.42, 0.42, 0.4]


def get_f_fern():
    p = random.uniform(0, 100)
    if p < 1.0:
        return f_1_f
    elif p < 86.0:
        return f_2_f
    elif p < 93.0:
        return f_3_f
    else:
        return f_4_f


def get_f_tree():
    p = random.uniform(0, 100)
    if p < 17.0:
        return f_1_t
    elif p < 34.0:
        return f_2_t
    elif p < 51.0:
        return f_3_t
    elif p < 68.0:
        return f_4_t
    elif p < 84.0:
        return f_5_t
    else:
        return f_6_t


def get_f_tree2():
    p = random.uniform(0, 100)
    if p < 25.0:
        return f_1_t2
    elif p < 50.0:
        return f_2_t2
    elif p < 75.0:
        return f_3_t2
    else:
        return f_4_t2


def iterate(x, y, mode):
    global color
    if mode == 1:
        color = 'mediumseagreen'
        for t in range(100000):
            f = get_f_fern()
            x1 = f[0] * x[t-1] + f[1] * y[t-1] + f[2]
            y1 = f[3] * x[t-1] + f[4] * y[t-1] + f[5]
            x.append(x1)
            y.append(y1)
    elif mode == 2:
        color = 'orchid'
        for t in range(100000):
            f = get_f_tree2()
            x1 = f[0] * x[t-1] + f[1] * y[t-1] + f[2]
            y1 = f[3] * x[t-1] + f[4] * y[t-1] + f[5]
            x.append(x1)
            y.append(y1)
    else:
        color = 'darkcyan'
        for t in range(100000):
            f = get_f_tree()
            x1 = f[0] * x[t-1] + f[1] * y[t-1] + f[2]
            y1 = f[3] * x[t-1] + f[4] * y[t-1] + f[5]
            x.append(x1)
            y.append(y1)


def main():
    iterate(X, Y, 2)
    plt.figure(figsize=[20, 20])
    plt.scatter(X, Y, color=color, marker='.')
    plt.show()


if __name__ == '__main__':
    main()
