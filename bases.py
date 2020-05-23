from math import sqrt, isclose


EPSILON = 0.00001


def equal(a,b):
    """
    checks if the two parameters are equal by using the Epsilon parameter of ten thousandth
    """
    if abs(a-b)<EPSILON:
        return True
    return False


class Tuple:
    def __init__(self, x, y, z, w):
        self.val = [x, y, z, w]

    def is_point(self):
        """
        checks if it is a point by checking the w component
        """
        return equal(self.val[3], 1)

    def is_vector(self):
        """
        checks if is a vector or not by checking the w component
        """
        return equal(self.val[3], 0)

    def __getitem__(self, item):
        """
        returns the value at the specific index
        0 for x
        1 for y
        2 for z
        3 for w
        """
        return self.val[item]

    def __eq__(self, other):
        """
        checks if the two tuples are equal or not
        """
        return(isclose(self.val[0], other.val[0])
               and isclose(self.val[1], other.val[1])
               and isclose(self.val[2], other.val[2])
               and isclose(self.val[3], other.val[3]))

    def __sub__(self, other):
        """
        returns binary subtraction of two tuples
        """
        x = self.val[0] - other.val[0]
        y = self.val[1] - other.val[1]
        z = self.val[2] - other.val[2]
        w = self.val[3] - other.val[3]
        return Tuple(x, y, z, w)

    def __add__(self, other):
        """
        returns the binary addition of tuples
        """
        x = self.val[0] + other.val[0]
        y = self.val[1] + other.val[1]
        z = self.val[2] + other.val[2]
        w = self.val[3] + other.val[3]
        return Tuple(x, y, z, w)

    def __neg__(self):
        """
        returns the negated value of the tuple, unary

        COULD BE A POSSIBLE ERROR SINCE THE SELF.VAL[3] IS NOT NEGATED
        BE AWARRRREEEE OF THISSSSSSS
        """
        return Tuple(-self.val[0], -self.val[1], -self.val[2], self.val[3])

    def __mul__(self, other):
        """
        returns the unary multiply on tuples
        """
        x = self.val[0] * other
        y = self.val[1] * other
        z = self.val[2] * other
        w = self.val[3] * other
        return Tuple(x, y, z, w)

    def __truediv__(self, other):
        """
        returns the unary divide operations
        """
        x = self.val[0] / other
        y = self.val[1] / other
        z = self.val[2] / other
        w = self.val[3] / other
        return Tuple(x, y, z, w)

    def magnitude(self):
        """
        returns only the magnitude of vectors
        """
        assert(self.is_vector())
        return sqrt(self.val[0]**2 + self.val[1]**2 + self.val[2]**2)

    def normalize(self):
        """
        Returns the normalized value in terms of the unit vector
        """
        assert(self.is_vector())
        mag = self.magnitude()
        return vector(self.val[0]/mag,
                     self.val[1]/mag,
                     self.val[2]/mag,
                     self.val[3]/mag)

    def __str__(self):
        return '{}'.format(self.val)

    def dot(self, other):
        """
        returns the dot product of two tuples
        """
        total = 0
        for i in range(3):
            total += self.val[i] * other.val[i]
        return total

    def reflect(self, normal):
        return self - normal * 2 * self.dot(normal)


class point(Tuple):
    def __init__(self, x, y, z, w=1.0):
        """
        sets the w component to zero for a point
        """
        super().__init__(x, y, z, w)


class vector(Tuple):
    def __init__(self, x, y, z, w=0.0):
        """
        sets the w value for the vector to 0
        """
        super().__init__(x, y, z, w)

    def cross(self, other):
        """
        can cross two vectors
        """
        assert(self.is_vector() and other.is_vector())
        return vector(self.val[1]*other.val[2] - self.val[2]*other.val[1],
                      self.val[2]*other.val[0] - self.val[0]*other.val[2],
                      self.val[0]*other.val[1] - self.val[1]*other.val[0])


def IdentifyHit(intersections):
    bestHit = None
    for intersection in intersections:
        if intersection['time'] < 0:
            continue
        if not bestHit or bestHit['time'] > intersection['time']:
            bestHit = intersection
    return bestHit



if __name__ == '__main__':
    """
    Testing for the above functions, you can play around with them
    """
    v = vector(0, -1, 0)
    n = vector(sqrt(2)/2, sqrt(2)/2, 0)
    r = v.reflect(n)
    print(r)
    # x = point(1, 1, 1)
    # a = vector(2, 3, 4)
    # b = vector(2, 3, 4)
    # print(a.dot(b))
    # y = vector(2, 2, 2)
    # a = point(1, 1, 1)
    # z = vector(6, 36, 2)
    # print(x)
    # print(y)
    # print(x.is_point(), x.is_vector())
    # print(y.is_point(), y.is_vector())
    # print(a == x)
    # print(a == y)
    # print(x-a)
    # print(x-y)
    # print(y-x)
    # print(-x)
    # print(x)
    # print(x*2)
    # print(x/2)
    # print(y.magnitude())
    # print(y.normalize())
    # print(y.dot(z))
    # print(y.cross(z))
