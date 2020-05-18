from ray_sphere import ray, sphere
from canvas_color import color, canvas
from bases import point, vector
import time
from light_shading import material, upscale_color, lighting, point_light, normal_at


tic = time.time()


""" 
canvas colour to be added in terms of 255 scale
but ibject colour has to be below 1 scale
"""
ray_origin = point(0, 0, -8)
wall_z = 10
wall_size = 7
canvas_pixels = 500
pixel_size = wall_size/canvas_pixels
half = wall_size / 2
canv = canvas(canvas_pixels, canvas_pixels, 0, 50, 9)
shape = sphere()

light_position = point(-10, 10, -10)
light_color = color(0.6, 0.6, 0.6)
light = point_light(light_position, light_color)

m = material()
shape.material = m
m.colour = color(1, 0, 0)  # is a hue of red color

for y in range(canvas_pixels):
    world_y = half - pixel_size * y
    print('row {} of {}'.format(y, canvas_pixels))
    for x in range(canvas_pixels):
        world_x = -half + pixel_size * x
        position = point(world_x, world_y, wall_z)
        position = position - ray_origin
        r = ray(ray_origin, position.normalize())
        xs = shape.intersect(r)
        if xs:
            point_col = r.position(xs[0])
            normal = normal_at(xs[2], point_col)
            eye = r.direction * -1
            bright = lighting(xs[2].material, light, point_col, eye, normal)
            bright = upscale_color(bright)
            bright = m.colour.multiply(bright)
            canv.write_canvas(x, y, bright)

canv.to_ppm(filename='BD_flag_3D')
toc = time.time()
print(round(toc-tic, 4))
