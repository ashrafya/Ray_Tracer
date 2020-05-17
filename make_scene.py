from ray_sphere import *
from light_shading import *
from bases import *
from canvas_color import *
from matrix_transformations import *
from math import ceil, pi, tan
import time


class world:
    def __init__(self, item=None, light=None):
        """
        initializes the world object with no shapes or light sources as default
        """
        self.objects = []
        if item is not None:
            self.objects.append(item)
        self.light = light

    def __str__(self):
        return 'world contains objects = {}\nworld has light source = {}'.format(self.objects[::], self.light)

    def add_object(self, item):
        """
        function to add an object to the world
        """
        self.objects.append(item)

    def add_light_source(self, light):
        """
        function to add a light source in the world
        """
        self.light = light

    def intersect_world(self, r):
        """
        returns a list of all the hits the ray has with all the objects in ascending order
        """
        all_hits = []
        for i in range(len(self.objects)):
            current_item = self.objects[i]   # this is currently the circle
            # print(self.objects[i])
            result = current_item.intersect(r)
            if result:   # meaning that if there are any hits that are returned by the intersect function above
                all_hits.append(result[0])
                all_hits.append(result[1])
        return sorted(all_hits)


class computation:
    def __init__(self, t=0, item=0, mark=0, eyev=0, normalv=0, inside=None):
        """
        item represents object
        mark represents point
        """
        self.t = t
        self.object = item
        self.point = mark
        self.eyev = eyev
        self.normalv = normalv
        self.inside = inside

    def __str__(self):
        return 't = {}\nobject = {}\npoint = {}\neyev = {}\nnormalv = {}'.format(self.t, self.object, self.point,
                                                                                 self.eyev, self.normalv)

    def prepare_computations(self, intersection, r):
        """
        returns precomputed shading information about the intersection in the form of the computation data structure
        """
        # initiate a data structure for storing the precomputed values
        # comps = computation()

        # copy the intersection's properties for convenience
        self.t = intersection.t
        self.object = intersection.items

        # precompute some useful values
        self.point = r.position(self.t)
        self.eyev = r.direction * -1
        self.normalv = normal_at(self.object, self.point)
        if self.normalv.dot(self.eyev) < 0:
            self.inside = True
            self.normalv = -self.normalv
        else:
            self.inside = False


def shade_hit(w, comps):
    """
    function returns the color at the intersection encapsulated by comps in the given world
    """
    return lighting(comps.object.material, w.light, comps.point, comps.eyev, comps.normalv)


def default_world():
    light = point_light(point(-5, 5, -5), color(1, 1, 1))
    m = translation(-2, -2, 2) * scaling(2, 2, 2)
    m2 = translation(2, -1, -1) * scaling(1.3, 1.3, 1.3)

    s1 = sphere(transform_within=m)
    s1.material.colour = color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    # m = matrix(4, 4, (transform(-2, -2, 2) * scaling(2, 2, 2)))
    s1.transform_within = m

    w = world()
    w.add_object(s1)

    s2 = sphere(transform_within=m2)
    s2.material.colour = color(1, 0.2, 1)
    s2.material.diffuse = 0.7
    s2.material.specular = 0.2

    w.add_object(s2)
    w.add_light_source(light)
    w.add_light_source(light)
    return w


def color_at(w, r):
    """
    takes in world and ray and returns the color at the closest hit
    """
    all_hits = w.intersect_world(r)
    lowest = 0
    index = 0
    if len(all_hits) == 0:
        return color(0, 0, 0)  # returning black
    for i in range(len(all_hits)):
        if all_hits[i] >= 0:
            lowest = all_hits[i]
            index = i
            break
    true_index = ceil(index/2)
    comps = computation()
    i = Intersection(lowest, w.objects[true_index])
    comps.prepare_computations(i, r)
    return shade_hit(w, comps)


def view_transform(From, to, up):
    v = (to - From)
    forward = v.normalize()
    upn = up.normalize()
    forward = vector(forward.val[0], forward.val[1], forward.val[2])
    upn = vector(upn.val[0], upn.val[1], upn.val[2])
    left = forward.cross(upn)
    true_up = left.cross(forward)
    orientation = matrix(4, 4, ([[left.val[0], left.val[1], left.val[2], 0],
                                 [true_up.val[0], true_up.val[1], true_up.val[2], 0],
                                 [-forward.val[0], -forward.val[1], -forward.val[2], 0],
                                 [0, 0, 0, 1]]))
    return orientation * translation(-From.val[0], -From.val[1], -From.val[2])


class camera:
    def __init__(self, hsize=160, vsize=120, filed_of_view=pi/2, transform=identity_matrix, pixel_size=None, half_view=None, half_height=None):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = filed_of_view
        self.transform = transform
        self.pixel_size = pixel_size
        self.half_width = half_view
        self.half_height = half_height
        self.set_pixel_size(self.hsize, self.vsize, self.field_of_view)

    def __str__(self):
        return 'horizontal = {}\nvertical = {}\nfield_of_view = {}\nTransform = {}\npixel_size = {}\nhalf_width = {}' \
               '\nhalf_height = {}'.format(self.hsize, self.vsize, self.field_of_view, self.transform, self.pixel_size,
                                           self.half_width, self.half_height)

    def set_pixel_size(self, horiontal, vertical, view_angle):
        half_view = tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view/aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / self.hsize


def ray_for_pixel(c, px, py):
    # the offset from the edge of teh canvas to the pixel's center
    xoffset = (px + 0.5) * c.pixel_size
    yoffset = (py + 0.5) * c.pixel_size

    # the untransformed coordinates of the pixel in world space. (the camera looks towards -z, so +x is to the left)
    world_x = c.half_width - xoffset
    world_y = c.half_height - yoffset

    # using the camera matrix, transform the canvas point and the origin, and then compute the ray's
    # direction vector
    pixel = c.transform.inverse().multiply_tuple(point(world_x, world_y, -1))
    origin = c.transform.inverse().multiply_tuple(point(0, 0, 0))
    direction = pixel - origin
    direction = vector(direction.val[0], direction.val[1], direction.val[2])
    direction = direction.normalize()
    return ray(origin, direction)


def render(c, w, filename='default_world'):
    """
    an image is rendered with a default canvas color of black
    """
    tic = time.time()
    image = canvas(c.hsize, c.vsize)
    for y in range(c.vsize):
        print('on line {} of {}'.format(y + 1, c.vsize))
        for x in range(c.hsize):
            r = ray_for_pixel(c, x, y)
            COL = color_at(w, r)
            COL = upscale_color(COL)
            image.write_canvas(x, y, COL)
    toc = time.time()
    print('it took {} seconds'.format(round(toc-tic, 2)))
    return image.to_ppm(filename=filename)



if __name__ == '__main__':
    w = world()
    # s = sphere()
    # s2 = sphere()
    # print(w)
    # print()
    # w.add_object(s)
    # print(w)
    # print()
    # w.add_object(s2)
    # print(w)

    # light = point_light(point(-10, 10, -10), color(1, 1, 1))
    # print(light.intensity)
    # s = sphere()
    # m = material(colour=color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
    # s.material = m
    # s2 = sphere(transform_within=scaling(0.5, 0.5, 0.5))
    # w = world(item=s)
    # w.add_object(s2)
    # w.add_light_source(light)

    # print(w)
    # print()
    # r = ray(point(0, 0, -5), vector(0, 0, 1))
    # print(w.intersect_world(r))

    # r = ray(point(0, 0, -5), vector(0, 0, 1))
    # shape = sphere()
    # i = Intersection(4, shape)
    # comps = computation()
    # comps.prepare_computations(i, r)
    # print(comps.t, comps.object, comps.point)
    # print(comps.normalv)
    # print(comps.eyev, comps.normalv)

    # r = ray(point(0, 0, 0), vector(0, 0, 1))
    # shape = sphere()
    # i = Intersection(1, shape)
    # comps = computation()
    # comps.prepare_computations(i, r)
    # print(shade_hit(w, comps))

    # w = default_world()
    # r = ray(point(0, 0, -5), vector(
    # w.light = point_light(point(0, 0.25, 0), color(1, 1, 1))
    # r = ray(point(0, 0, 0), vector(0, 0, 1))
    # shape = w.objects[1]
    # i = Intersection(0.5, shape)
    # comps = computation()
    # comps.prepare_computations(i, r)
    # print(shade_hit(w, comps))0, 0, 1))
    # shape = w.objects[0]
    # i = Intersection(4, shape)
    # comps = computation()
    # comps.prepare_computations(i, r)
    # print(shade_hit(w, comps))
    # w = default_world()

    # w = default_world()
    # r = ray(point(0, 0, 0.75), vector(0, 0, -1))
    # print(color_at(w, r))

    # From = point(1, 3, 2)
    # to = point(4, -2, 8)
    # up = vector(1, 1, 0)
    # print(view_transform(From, to, up))
    # c = camera(125, 1240, pi/2)
    # print(c)

    # c = camera(201, 101, pi/2)
    # c.transform = y_rotation(pi/4) * translation(0, -2, 5)
    # r = ray_for_pixel(c, 100, 50)
    # print(r)

    w = default_world()
    c = camera(400, 400, pi/3)
    FROM = point(0, 0, -5)
    to = point(0, 0, 0)
    up = vector(0, 1, 0)
    c.transform = view_transform(FROM, to, up)
    image = render(c, w)




    

