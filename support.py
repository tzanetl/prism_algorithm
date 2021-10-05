# Taneli Leppanen
# Algoririthmics for engineering informatics
# Taneli.Leppanen[at]student.tut.fi
# Task 3 - Prims algorithm with euclidian distance


from random import randint
from Vertex import *
import matplotlib.pyplot as plt
import itertools


# Initializes the point space with random points
def initSpace(xmax, ymax, points):
    point_list = []

    for i in range(points):
        vertex = Vertex(randint(1, xmax - 1), randint(1, ymax - 1))
        point_list.append(vertex)

    print("Tree initialized")
    return point_list


# Calculates the distance between 2 points
def distance(x1, y1, x2, y2):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d


# Plots the tree
def plotTree(tree, xmax, ymax):
    xl = []
    yl = []

    # Adds to cordinates to their respective lists
    for b in tree:
        xl.append(b.x)
        yl.append(b.y)

        # Plots the connections
        if b.con is not None:
            plt.plot([b.x, b.con.x], [b.y, b.con.y], 'k-', linewidth=2.0)

    plt.plot(xl, yl, 'ko', ms=10)     # Plot points
    plt.axis([0, xmax, 0, ymax])      # Set axis
    plt.grid(True)
    plt.title('Minimum Spanning 2D Tree')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    print("Tree plotted to graph")
    plt.show()


# Source: https://stackoverflow.com/questions/6834483/how-do-you-create-line-segments-between-two-points
def plotScatter(pl, xmax, ymax):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    all_data = []

    for p in pl:
        l = []
        l.append(p.x)
        l.append(p.y)
        all_data.append(l)

    plt.plot(
        *zip(*itertools.chain.from_iterable(
            itertools.combinations(all_data, 2))),
        color='k', marker='o', ms=10)

    plt.grid(True)
    plt.axis([0, xmax, 0, ymax])
    plt.title('All Possible Connections')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    plt.show()