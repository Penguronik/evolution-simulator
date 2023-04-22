import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib import style


style.use('bmh')


fig = plt.figure()

#ax1 = fig.add_subplot(1, 1, 1)

#ax1.plot([1, 3, 2, 4], [1, 9, 4, 16])

plt.ylabel('numbers')

plt.xlabel('some')

plt.title('hello')


def animate(i):

    graph_data = open('example.txt', 'r').read()

    lines = graph_data.split('\n')

    xs = []

    ys = []

    for line in lines:

        if len(line) > 1:

            x, y = line.split(',')

            xs.append(int(x))

            ys.append(int(y))

    plt.cla()

    plt.plot(xs, ys)

    plt.ylabel('Population')

    plt.xlabel('Round Counter')

    plt.title('Population Over Time')


ani = animation.FuncAnimation(fig, animate, interval=100)


plt.show()
