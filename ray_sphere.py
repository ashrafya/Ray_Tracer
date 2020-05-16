from bases import point, vector
from math import sqrt
from matrices import matrix, identity_matrix
from matrix_transformations import translation, scaling

# transform_ within == transform attribute for sphere class


class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, time):
        """
        returns teh position after a number of seconds
        """
        # get start position in each direction
        zerox = self.origin.val[0]
        zeroy = self.origin.val[1]
        zeroz = self.origin.val[2]

        # find the vector moving in each direction
        x = (self.direction.val[0] * time) + zerox
        y = (self.direction.val[1] * time) + zeroy
        z = (self.direction.val[2] * time) + zeroz
        return point(x, y, z)

    def __str__(self):
        return 'start = {} \ndirection = {}'.format(self.origin, self.direction)


class sphere:
    """
    will assume origin of all circles is at (0, 0, 0)
    also assume they are unit circles with a radius of '1'
    """
    def __init__(self, radius=1, origin=([0, 0, 0])):
        self.radius = radius
        self.origin = origin
        self.transform_within = identity_matrix

    def __str__(self):
        return 'radius = {}\norigin = {}'.format(self.radius, self.origin)

    def set_transform(self, t):
        """
        modifies the self.transform)within value of the sphere, which is set to the identity matrix as a default
        """
        self.transform_within = t

    def intersect(self, ray):
        """
        returns the intersection between a sphere and ray
        returns an empty list if there are no intersections
        returns the same value in both indexes of the list if the ray hits the sphere on a tangent
        if the ray intersects the sphere at two points, the first value of the list is smaller
        """
        t = self.transform_within
        inv = t.inverse()
        direction = inv.multiply_tuple(ray.direction)
        origin = inv.multiply_tuple(ray.origin)
        sphere_to_ray = origin - point(0, 0, 0)
        a = direction.dot(direction)
        b = 2 * direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        det = b * b - 4 * a * c
        if det < 0:
            return []
        t1 = (-b - sqrt(det)) / (2 * a)
        t2 = (-b + sqrt(det)) / (2 * a)
        return [{'time': t1, 'object': self.__class__.__name__}, {'time': t2, 'object': self.__class__.__name__}]


class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object
        self.type = self.object.__class__.__name__

    def __str__(self):
        return 't = {}\nobject type = {}'.format(self.t, self.object.__class__.__name__)


def intersectionsss(inter_list):
    """
    returns a list of all intersection objects
    """
    return inter_list


def hit(hits):
    """
    returns the object with the lowest value of intersection that is above 0
    """
    lowest = hits[0].t
    count = 0
    index = 0
    for i in range(len(hits)):
        if lowest < 0:
            lowest = hits[i].t
        if 0 < hits[i].t <= lowest:
            lowest = hits[i].t
            count += 1
            index = i
    if count == 0 and lowest <= 0:
        return None
    return hits[index]


def transform(r, m):
    """
    returns a new transformed ray, with its point and vector attributes multiplied accordingly
    """
    new_origin = m.multiply_tuple(r.origin)
    new_direction = m.multiply_tuple(r.direction)
    return ray(new_origin, new_direction)


if __name__ == '__main__':
    """ 
    these are the tests I used to test the above functions and they can be played around with
    """
    p = point(0, 0, 0)
    # v = vector(0, 0, 1)
    # r = ray(p, v)
    # s = sphere()
    # print(s.transform_within)
    # i1 = Intersection(5, s)
    # i2 = Intersection(7, s)
    # i3 = Intersection(-3,s)
    # i4 = Intersection(2, s)
    # i5 = Intersection(1, s)
    # print(i3)
    # print(hit([i1, i2, i3, i4, i5]))
    # print(i1)
    # print(i2)
    # f = intersectionsss([i1, i2, i3])
    # print(f[0].type, f[1].type, f[2].type)
    # print(f[0], f[1])
    # print()
    # print(s.intersect(r))
    # p = point(0, 0, -5)
    # v = vector(0, 0, 1)
    # s = sphere()
    # p = point(1, 2, 3)
    # v = vector(0, 1, 0)
    # r = ray(p, v)
    # m = translation(3, 4, 5)
    # ms = scaling(2, 3, 4)
    # s.set_transform(m)
    # print()
    # print(s.transform_within)
    # r2 = transform(r, m)
    # print(r2.origin)
    # print(r2.direction)
    # p = point(0, 0, -5)
    # v = vector(0, 0, 1)
    # r = ray(p, v)
    # s = sphere()
    # s.set_transform(translation(5, 0, 0))
    # print(s.intersect(r))
