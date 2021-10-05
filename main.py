# Taneli Leppanen
# Algoririthmics for engineering informatics
# Taneli.Leppanen[at]student.tut.fi
# Task 3 - Prims algorithm with euclidian distance


from support import *
from prims import build


def main():

    xmax = 20
    ymax = 20
    points = 13

    point_list = initSpace(xmax, ymax, points)

    plotScatter(point_list, xmax, ymax)

    mst = build(point_list, xmax, ymax)

    plotTree(mst, xmax, ymax)

main()
