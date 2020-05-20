class Intersection:
    def __init__(self, time, object):
        self.t = time
        self.object = object

    # def __str__(self):
    #     return 'time = {}   object = {}'.format(self.t, self.object)


class Intersections:
    def __init__(self, *intersections):
        self.sorted_intersections = sorted(intersections, key=lambda i: i.t)
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
