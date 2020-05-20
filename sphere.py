from bases import point
from math import sqrt
from matrices import identity_matrix


class sphere:
    def __init__(self, transform_within=identity_matrix, material=None):
        """
        these values are set to none for now but will be changed in due time
        - transform_within has been set to the identity matrix
        """
        self.transform_within = transform_within
        self.material = material

    def Transform_Within(self):
        """
        returns the tranformation
        """
        return self.transform_within

    def set_transform(self, transform_to):
        self.transform_within = transform_to

    def sphere_material(self):
        return self.material

    def Count(self):
        return self.count

    def intersect(self, ray_initial):
        """
        The big intersect function that finds the intersection of a sphere and a ray
        two or zero intersections returned
            zero in teh case of no intersection
            two in the case of both a single and two unique intersections
            smaller first followed by larger intersection
        """
        r = ray_initial.transform(self.transform_within.inverse())
        sphere_to_ray = r.Origin() - point(0, 0, 0)
        a = r.Direction().dot(r.Direction())
        b = 2 * r.Direction().dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return ()
        t1 = (-b - sqrt(discriminant))/(2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)
        return [{'time': t1, 'object':self}, {'time': t2, 'object':self}]

    def local_normal(self, object_point):
        pass

    def __str__(self):
        return 'transform = {}\nmaterial = {}'.format(self.transform_within, self.material)


# if __name__ == '__main__':
#     r = ray(point(0, 0, -5), vector(0, 0, 1))
#     s = sphere()
#     s.set_transform(scaling(2, 2, 2))
#     xs = s.intersect(r)
#     print(xs[0]['time'])
#     print(xs[1]['time'])
