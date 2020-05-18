from ray_sphere import ray, sphere
from canvas_color import color, canvas
from bases import point, vector
import time

tic = time.time()
ray_origin = point(0, 0, -5)
wall_z = 10
wall_size = 7
canvas_pixels = 100
pixel_size = wall_size/canvas_pixels
half = wall_size / 2
red = color(255, 0, 0)
canv = canvas(canvas_pixels, canvas_pixels, 255, 255, 255)
shape = sphere()

for y in range(canvas_pixels):
    world_y = half - pixel_size * y
    for x in range(canvas_pixels):
        world_x = -half + pixel_size * x
        position = point(world_x, world_y, wall_z)
        position = position - ray_origin
        r = ray(ray_origin, position.normalize())
        xs = shape.intersect(r)
        if xs != []:
            canv.write_canvas(x, y, red)
canv.to_ppm(filename='japan_flag')
toc = time.time()
print(round(toc-tic, 4))
