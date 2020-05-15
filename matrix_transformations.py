from bases import point, vector
from matrices import matrix
from math import cos, sin, pi


def translation(x, y, z):
    """
    returns a transformation matrix
    """
    return matrix(4, 4, ([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]))


def scaling(x, y, z):
    """
    returns a scaling matrix
    """
    return matrix(4, 4, ([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]))


def x_rotation(rad):
    """
    returns a rotation matrix in teh x direction
    """
    return matrix(4, 4, ([[1, 0, 0, 0], [0, cos(rad), -sin(rad), 0], [0, sin(rad), cos(rad), 0], [0, 0, 0, 1]]))


def y_rotation(rad):
    """
    returns a rotation matrix in teh y direction
    """
    return matrix(4, 4, ([[cos(rad), 0, sin(rad), 0], [0, 1, 0, 0], [-sin(rad), 0, cos(rad), 0], [0, 0, 0, 1]]))


def z_rotation(rad):
    """
    returns a transformation matrix in the z direction
    """
    return matrix(4, 4, ([[cos(rad), -sin(rad), 0, 0], [sin(rad), cos(rad), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))


def shearing(xy, xz, yx, yz, zx, zy):
    """
    returns a shearing matrix
    """
    return matrix(4, 4, ([[1, xy, xz, 0], [yx, 1, yz, 0], [zx, zy, 1, 0], [0, 0, 0, 1]]))


def check_tuple(x, y, z, w):
    """
    checks if the tuple is a point or a vector
    """
    if w == 0:
        return vector(x, y, z)
    return point(x, y, z)


def to_matrix(Tuple):
    """
    converts a Tuple(point or a vector) into a matrix
    """
    return matrix(4, 4, ([[Tuple.val[0], 0, 0, 0], [0, Tuple.val[1], 0, 0], [0, 0, Tuple.val[2], 0], [0, 0, 0, Tuple.val[3]]]))


if __name__ == '__main__':
    """ 
    tests used to check if the above function are working or not
    """
    x = point(-3, 4, 5)
    # y = vector(-3, 4, 5)
    # z = translation(5, -3, 2)
    # inv = z.inverse()
    # print(inv.multiply_tuple(x))
    # print(x)
    # print(x, z)
    # print(z.multiply_tuple(x))
    # print(z.multiply_tuple(y))
    # print()
    # scale = scaling(2, 3, 4)
    # p = point(-4, 6, 8)
    # v = vector(-4, 6, 8)
    # print(scale.multiply_tuple(p))
    # print()
    # print(scale.multiply_tuple(v))
    # print()
    # inv = scale.inverse()
    # print(inv.multiply_tuple(v))
    # print()
    # new = point(2, 3, 4)
    # scale1 = scaling(-1, 1, 1)
    # print(scale1.multiply_tuple(new))
    # p = point(0, 1, 0)
    # half = x_rotation(pi/4)
    # full = x_rotation(pi/2)
    # print(half.multiply_tuple(p))
    # print()
    # print(full.multiply_tuple(p))
    # inv = half.inverse()
    # print()
    # print(inv.multiply_tuple(p))
    # p = point(0, 0, 1)
    # half = y_rotation(pi/4)
    # full = y_rotation(pi/2)
    # print(half.multiply_tuple(p))
    # print()
    # print(full.multiply_tuple(p))
    # inv = half.inverse()
    # print()
    # print(inv.multiply_tuple(p))
    # p = point(0, 1, 0)
    # half = z_rotation(pi/4)
    # full = z_rotation(pi/2)
    # print(half.multiply_tuple(p))
    # print(full.multiply_tuple(p))
    # p = point(2, 3, 4)
    # xy = shearing(1, 0, 0, 0, 0, 0)
    # xz = shearing(0, 1, 0, 0, 0, 0)
    # yx = shearing(0, 0, 1, 0, 0, 0)
    # yz = shearing(0, 0, 0, 1, 0, 0)
    # zx = shearing(0, 0, 0, 0, 1, 0)
    # zy = shearing(0, 0, 0, 0, 0, 1)
    # print(xy.multiply_tuple(p))
    # print(xz.multiply_tuple(p))
    # print(yx.multiply_tuple(p))
    # print(yz.multiply_tuple(p))
    # print(zx.multiply_tuple(p))
    # print(zy.multiply_tuple(p))
    # p = point(1, 0, 1)
    # rot = x_rotation(pi/2)
    # scale = scaling(5, 5, 5)
    # trans = translation(10, 5, 7)
    # p2 = rot.multiply_tuple(p)
    # print(p2)
    # print()
    # p3 = scale.multiply_tuple(p2)
    # print(p3)
    # print()
    # p4 = trans.multiply_tuple(p3)
    # print(p4)
