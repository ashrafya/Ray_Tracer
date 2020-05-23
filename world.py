from material import point_light
from bases import point, vector
from canvas_color import color
from sphere import sphere
from matrix_transformations import scaling, translation, view_transform
from ray import ray
from Intersection import Intersection, Intersections
from operator import itemgetter

class world:
    def __init__(self, object=[], light=[]):
        self.items = object
        self.light = light

    def Num_objects(self):
        return len(self.object)

    def set_light(self, light):
        self.light = [light]
    
    def Num_lights(self):
        return len(self.light)

    def Lights(self):
        return self.light

    def Items(self):
        return self.items

    def add_object(self, object):
        self.items += [object]

    def intersect_world(self, r):
        """
        takes in a ray and teh world object adn returns all teh intersection between the world and
            ray in sorted order
        """
        joints = []
        for item in self.Items():
            x = item.intersect(r)
            if x != ():
                joints.append(x[0])
                joints.append(x[1])
        if joints == []:
            return joints
        joints.sort(key=itemgetter('time'))
        return joints

    def shade_hit(self, computations):
        """
        returns the shade that should be painted at that point of hit
        """
        return computations['object'].material.Lighting(self.light[0], computations['point'], computations['eyev'], computations['normalv'])

    def color_at(self, r):
        """
        tieing up the intersect(), shade_hit(), and prepare_computations() functions for convenience's sake
        """
        # getting all the hits in total
        total_junctions = self.intersect_world(r)
        first = True
        if len(total_junctions) > 0:
            for hit in total_junctions:
                if hit['time'] >=0 and first == True:
                    i = Intersection(hit['time'], hit['object'])
                    first = False

        if first == True or len(total_junctions) == 0:
            return color(0, 0, 0)

        comps = i.prepare_computations(r)

        # call shade_hit() to return the color at that specific point
        COL = self.shade_hit(comps)
        return COL

    # have the view transform function in the matrix_transformation.py file



def default_world():
    light = point_light(point(-10, 10, -10), color(1, 1, 1))
    s1 = sphere()
    s1.material.colour = color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = sphere()
    s2.transform_within = scaling(0.5, 0.5, 0.5)
    w = world(object=[s1, s2], light=[light])
    return w


if __name__ == '__main__':
    # w = default_world()
    # w.set_light(point_light(point(0, 0.25, 0), color(1, 1, 1)))
    # r = ray(point(0, 0, 0), vector(0, 0, 1))
    # i = Intersection(0.5, w.items[1])
    # comps = i.prepare_computations(r)
    # c = w.shade_hit(comps)
    # print(c)

    w = default_world()
    x =w.Items()
    r = ray(point(0, 0, -5), vector(0, 0, 1))
    c = w.color_at(r)
    print(c.red, c.green, c.blue)



