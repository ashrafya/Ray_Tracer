from matrices import identity_matrix
from material import material


class shape:
    def __init__(self, transform_within=None, set_material=None):
        if transform_within == None:
            self.transform_within = identity_matrix
        else:
            self.transform_within = transform_within
        if set_material == None:
            self.set_material = material()
        else:
            self.set_material = set_material

    def fuck_it(self):
        print('fuck it')


if __name__ == '__main__':
    s = shape()
    s.fuck_it()
