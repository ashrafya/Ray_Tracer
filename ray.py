from bases import point, vector
from matrix_transformations import scaling

class ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def __str__(self):
        """
        prints the objects in the ray
        """
        return 'origin = {}    direction = {}'.format(self.origin, self.direction)

    def Origin(self):
        """
        check what the origin is in the ray
        """
        return self.origin

    def Direction(self):
        """
        check the direcrion of the ray
        """
        return self.direction

    def position(self, time):
        """
        returns a point at t second along the origin and direction of the ray
        """
        final = self.origin + (self.direction * time)
        return final

    def transform(self, matrix):
        """
        returns a second transformed ray
        """
        return ray(matrix.multiply_tuple(self.origin), matrix.multiply_tuple(self.direction))


if __name__ == '__main__':
    r = ray(point(1, 2, 3), vector(0, 1, 0))
    m = scaling(2, 3, 4)
    r2 = r.transform(m)
    print(r2.origin, r.origin)
    print(r2.direction, r.direction)
