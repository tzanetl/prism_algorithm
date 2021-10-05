# Taneli Leppanen
# Algoririthmics for engineering informatics
# Taneli.Leppanen[at]student.tut.fi
# Task 3 - Prims algorithm with euclidian distance


from support import distance


# Builds a tree from list of points
def build(pl, xmax, ymax):
    tree = []
    # Remove 1st element from list containing points and add to tree as
    # startign point
    tree.append(pl.pop(0))

    while len(pl) > 0:
        # Find closest point and connection
        pc, bc = closest(pl, tree, xmax, ymax)
        pl.remove(pc)   # Remove closest point from point list
        pc.con = bc     # Add connection point to closest point
        tree.append(pc)     # Add new branch to tree

    print("Tree built")
    return tree


# Finds the closest point to current tree branches and where it connects in
# the tree
def closest(pl, tree, xmax, ymax):
    dc = xmax * ymax    # Distance Closest

    for p in pl:    # For Point in Point List

        for b in tree:  # For Branch in tree
            d = distance(p.x, p.y, b.x, b.y)

            if d < dc:
                dc = 0 + d
                pc = p  # Point Closest
                bc = b  # Branch Connection

    return pc, bc
