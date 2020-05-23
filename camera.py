from math import pi, tan
from matrices import identity_matrix
from bases import point
from ray import ray
from canvas_color import canvas, color


class camera:
    def __init__(self, hsize=160, vsize=120, field_of_view=pi/2, set_transform=identity_matrix):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.set_transform = set_transform
        half_view = tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / self.hsize

    def Half_Width(self):
        return self.half_width

    def Half_Height(self):
        return self.half_height

    def Hsize(self):
        return self.hsize

    def Vsize(self):
        return self.vsize

    def Field_Of_View(self):
        return self.field_of_view

    def Set_Transform(self, MAT):
        self.set_transform = MAT

    def What_Set_Transform(self):
        return self.set_transform

    def Get_Pixel_Size(self):
        return self.pixel_size

    def ray_for_pixel(self, px, py):
        xoffset = (px + 0.5) * self.Get_Pixel_Size()
        yoffset = (py + 0.5) * self.Get_Pixel_Size()

        world_x = self.Half_Width() - xoffset
        world_y = self.Half_Height() - yoffset

        pixel = self.set_transform.inverse().multiply_tuple( point(world_x, world_y, -1) )
        origin = self.set_transform.inverse().multiply_tuple( point(0, 0, 0) )

        direction = pixel - origin
        direction = direction.normalize()

        return ray(origin, direction)

    def render(self, w):
        """
        draws this on a canvas, given a world and teh view of the camera
        """
        image = canvas(height=self.vsize, width=self.hsize)
        for y in range(self.vsize):
            print('line {} of {}'.format(y+1, self.vsize))
            for x in range(self.hsize):
                r = self.ray_for_pixel(x, y) # r is the ray
                COL = w.color_at(r)
                red = COL.red * 255
                green = COL.green * 255
                blue = COL.blue * 255
                if red > 255:
                    red = 255
                if green > 255:
                    green = 255
                if blue > 255:
                    blue = 255
                COLOR = color(red, green, blue)
                image.write_canvas(x, y, COLOR)

        return image


# if __name__ == '__main__':
#     w = default_world()
#     c = camera(11, 11)
#     FROM = point(0, 0, -5)
#     TO = point(0, 0, 0)
#     UP = vector(0, 1, 0)
#     c.Set_Transform(view_transform(FROM, TO, UP))
#     IMG = c.render(w)


#     c = camera(hsize=201, vsize=101, field_of_view=pi/2)
#     c.Set_Transform(y_rotation(pi / 4) * translation(0, -2, 5))
#     r = c.ray_for_pixel(100, 50)
#     print(r.origin)
#     print(r.direction)


