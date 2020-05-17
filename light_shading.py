from bases import point, vector
from canvas_color import color
import ray_sphere
from math import sqrt, pi, pow
from matrix_transformations import translation, scaling, z_rotation


class point_light:
    """
    structure of a light source defaulted to origin (0, 0, 0) and intensity is both intensity and the color
        of the light source
    """
    def __init__(self, position=point(0, 0, 0), intensity=color(1, 1, 1)):
        self.position = position
        self.intensity = intensity

    def __str__(self):
        return 'position = {}\nintensity = {}'.format(self.position, self.intensity)


class material:
    """
    material structure taht has been set to default setting according to the Phong reflection method
    the arguments it takes are also an implementation of the Phong reflection method
    """
    def __init__(self, colour=color(1, 1, 1), ambient=0.1, diffuse=0.9, specular=0.9, shininess=200.0):
        self.colour = colour
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __str__(self):
        return'color={}\nambient={}\ndiffuse={}\nspecular={}\nshininess={}'.format(self.colour, self.ambient,
                                                                                   self.diffuse, self.specular,
                                                                                   self.shininess)


def normal_at(s, p):
    """
    s is the sphere and p represents the point
    this returns the normal at the point, i.e. a normalized vector
    this also takes into account any transformation or scaling that is applied to the sphere
    """
    object_point = s.transform_within.inverse().multiply_tuple(p)
    object_normal = object_point - point(0, 0, 0)
    world_normal = s.transform_within.inverse().transpose().multiply_tuple(object_normal)
    world_normal.val[3] = 0.0
    return world_normal.normalize()


def reflect(in_vector, normal):
    """
    returns the reflected vector given the incoming vector and the normal vector of the
        surface of the object at that point
    """
    temp = in_vector.dot(normal)
    temp = temp * 2
    temp = normal * temp
    return in_vector - temp


def lighting(object_material, light, point_on, eyev, normalv):
    """ 
    light is the point light structure passed into the function
    """
    black = color(0, 0, 0)
    # combine surface color intensity with light color intensity
    effective_color = object_material.colour.multiply(light.intensity)

    # find direction to the light source
    lightv = light.position - point_on
    lightv = lightv.normalize()

    # compute light color
    ambient = effective_color * object_material.ambient

    # light_dot_normal represents the cosine of the angle between the light vector and the normal vector. a negative
    # number means the light is on the other side of teh surface
    light_dot_normal = lightv.dot(normalv)

    if light_dot_normal < 0:
        diffuse = black
        specular = black
    else:
        # compute diffuse contribution
        diffuse = effective_color * object_material.diffuse
        diffuse = diffuse * light_dot_normal

        # reflect_dot_eye represents the cosine of the angle between the reflection vector and the eye vector. A
        # negative number means the light reflects away from the eye
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = reflectv.dot(eyev)
        if reflect_dot_eye <= 0:
            specular = black
        else:
            # compute teh specular contribution
            factor = pow(reflect_dot_eye, object_material.shininess)
            specular = light.intensity * object_material.specular * factor
    return ambient + diffuse + specular


def upscale_color(col):
    # highest = 0
    # if col.red > highest:
    #     highest = col.red
    # if col.green > highest:
    #     highest = col.green
    # if col.blue > highest:
    #     highest = col.blue
    # if highest == 0:
    #     return color(col.red, col.green, col.blue)
    red = col.red * 255
    green = col.green * 255
    blue = col.blue * 255

    return color(red, green, blue)




if __name__ == '__main__':
    # pl = point_light(intensity=color(1, 1, 1))
    # m = material()
    # s = ray_sphere.sphere()
    # m = material(ambient=1)
    # print(s)
    # print()
    # print(m)
    # s.material = m
    # print()
    # print(s)
    # p = point(0, sqrt(2)/2, -sqrt(2)/2)
    # m = scaling(1, 0.5, 1) * z_rotation(pi/5)
    # s.set_transform(m)
    # print(normal_at(s, p))
    # v = vector(0, -1, 0)
    # n = vector(sqrt(2)/2, sqrt(2)/2, 0)
    # print(reflect(v, n))
    m = material()
    position = point(0, 0, 0)
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    p = point(0, 0, 10)
    c = color(1, 1, 1)
    light = point_light(p, c)
    z = lighting(m, light, position, eyev, normalv)
    print(z)
    print(z.red, z.green, z.blue)
