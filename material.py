from canvas_color import color
from matrices import identity_matrix
from math import pow


class point_light:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def Position(self):
        return self.position

    def Intensity(self):
        return self.intensity


class material:
    def __init__(self, colour=color(1, 1, 1), ambient=0.1, diffuse=0.9, specular=0.9, shininess=200.0):
        self.colour = colour
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def Colour(self):
        return self.colour

    def set_colour(self, col):
        self.colour = col

    def Ambient(self):
        return self.ambient

    def set_ambient(self, amb):
        self.ambient = amb

    def Diffuse(self):
        return self.diffuse

    def set_diffuse(self, diff):
        self.diffuse = diff

    def Specular(self):
        return self.specular

    def set_specular(self, spec):
        self.specular = spec

    def Shininess(self):
        return self.shininess

    def set_shininess(self, shin):
        self.shininess = shin

    def Lighting(self, light, position, eyev, normalv, in_shadow=False, objectTransform=identity_matrix):
        """
        the phong algorithm implementation to get back 3D lighting simulation
        """
        # combine the surface colour and light colour
        effective_color = self.colour.multiply(light.Intensity())

        # find the direction to the light source
        lightv = light.Position() - position
        lightv = lightv.normalize()

        # compute the ambient color
        ambient = effective_color * self.Ambient()

        if in_shadow:
            return ambient

        # light_dot_normal represents the cosine of the angle between the light vector and teh normal vector.
        # a negative number means the light is on the other side of the surface
        light_dot_normal = lightv.dot(normalv)
        black = color(0, 0, 0)
        if light_dot_normal < 0:
            diffuse = black
            specular = black
        else:
            # compute the diffuse contribution
            diffuse = effective_color * self.Diffuse() * light_dot_normal

            # reflect_dot_eye represents the cosine  of the angle between the reflection vector and the eye vector
            # A negative number means the light reflects away form the eye
            reflectv = lightv * -1
            reflectv = reflectv.reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)

            if reflect_dot_eye <= 0:
                specular = black
            else:
                # compute the specular contribution
                factor = pow(reflect_dot_eye, self.Shininess())
                specular = light.intensity * self.Specular() * factor
        result = ambient + diffuse + specular
        return result
