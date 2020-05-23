from bases import point, vector, EPSILON
from ray import ray
from sphere import sphere


class Intersection:
    def __init__(self, time, object):
        self.t = time
        self.object = object

    # def __str__(self):
    #     return 'time = {}   object = {}'.format(self.t, self.object)

    def prepare_computations(self, ray):
        computations = {}
        computations['time'] = self.t
        computations['object'] = self.object
        computations['point'] = ray.position(computations['time'])
        computations['eyev'] = -ray.Direction()
        computations['normalv'] = self.object.normal_at(computations['point'])
        computations['inside'] = computations['normalv'].dot(computations['eyev']) < 0
        if computations['inside']:
            computations['normalv'] = -computations['normalv']
        computations['over_point'] = computations['point'] + (computations['normalv'] * EPSILON)
        return computations

class Intersections:
    def __init__(self, *intersections):
        self.sorted_intersections = sorted(intersections[::], key=lambda i: i.t)
        self.count = len(self)

    def __len__(self):
        return len(self.sorted_intersections)

    def __getitem__(self, key):
        return self.sorted_intersections[key]

    def hit(self):
        xs = list(filter(lambda x: x.t >= 0, self.sorted_intersections))

        if len(xs) < 1:
            return None

        return xs[0]


# if __name__ == '__main__':
#     r = ray(point(0, 0, -5), vector(0, 0, 1))
#     shape = sphere()
#     i = Intersection(4, shape)
#     comps = i.prepare_computations(r)
#     print(comps['time'])
#     print(comps['object'])
#     print(comps['point'])
#     print(comps['eyev'])
#     print(comps['normalv'])
#     print(comps['inside'])
