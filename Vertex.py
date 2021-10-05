# Taneli Leppanen
# Algoririthmics for engineering informatics
# Taneli.Leppanen[at]student.tut.fi
# Task 3 - Prims algorithm with euclidian distance


# Class that stores the coordinates and where it connects in the tree
class Vertex(object):

    def __init__(self, x=None, y=None, con=None):
        self.x = x
        self.y = y
        self.con = con

    # For printing the Vertex
    def __str__(self):

        if self.con is not None:
            s = "Vertex:\n" \
                "   cor: ({0}, {1})\n" \
                "   con: ({2}, {3})"\
                .format(self.x, self.y, self.con.x, self.con.y)
        else:
            s = "Vertex:\n" \
                "   cor: ({0}, {1})".format(self.x, self.y)

        return s
