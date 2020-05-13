# create tuples with (x,y,z,w)
# w==1 (is a point)
# w==0 (is a vector)
EPSILON = 0.00001

import math

def equal(a,b):
    if abs(a-b)<EPSILON:
        return True
    return False


class point:
    """
    represents a point that can be made with tuple
    """
    def __init__(self, x=0.0, y=0.0, z=0.0, w=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        # print('the POINT as the following values')
        # print('x:%s' % self.x)
        # print('y:%s' % self.y)
        # print('z:%s' % self.z)

    def __sub__(self, other):
        """
        unary negative
        """
        if other.w != 0:
            # subtracting a vector from a point gives us a vector
            x_val = self.x - other.x
            y_val = self.y - other.y
            z_val = self.z - other.z
            return vector(x_val, y_val, z_val)
        elif other.w == 0:
            # subtracting a point from a point gives us a point
            x_val = self.x - other.x
            y_val = self.y - other.y
            z_val = self.z - other.z
            return point(x_val, y_val, z_val)

    def __neg__(self):
        return point(self.x*-1, self.y*-1, self.z*-1, self.w*-1)


class vector:
    """
    represents a point that can be made with tuple
    """

    def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        # print('the VECTOR as the following values')
        # print('x:%s' % self.x)
        # print('y:%s' % self.y)
        # print('z:%s' % self.z)

    def __sub__(self, other):
        """
        unary negative
        """
        val_x = self.x - other.x
        val_y = self.y - other.y
        val_z= self.z - other.z
        return vector(val_x, val_y, val_z)

    def __neg__(self):
        return vector(self.x*-1, self.y*-1, self.z*-1, self.w*-1)

    def __mul__(self, other):
        """
        has to be in the order that vector times scalar
        """
        return vector(self.x*other, self.y*other, self.z*other, self.w*other)

    def magnitude(self):
        return math.sqrt((self.x**2) + (self.y**2) + (self.z**2))

    def normalize(self):
        mag = self.magnitude()
        return vector(self.x/mag,self.y/mag, self.z/mag, self.w/mag)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w
    
    def cross(self, other):
        return vector(self.y * other.z - self.z * other.y, (self.z * other.x) - (self.x * other.z),\
                      (self.x * other.y) - (self.y * other.x))


if __name__ == "__main__":
    x = point(2,3,3)
    y = point(1,1,1)
    vec = vector(4,3,7)
    vec2 = vector(12,20,20)
    final = vec - vec2
    print(final.x, final.y, final.z)
    z = x-y
    print(vec.x, vec.y, vec.z, vec.w)
    print(z.x, z.y, z.z)
    print(vec.magnitude())
    new = vec.normalize()
    print(new.x, new.y, new.z, new.w)
    first = vector(1,2,3)
    second = vector(2,3,4)
    print(first.dot(second))
    damn = second.cross(first)
    print(damn.x, damn.y, damn.z)