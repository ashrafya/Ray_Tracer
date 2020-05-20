from bases import point
from canvas_color import color, canvas
from sphere import sphere
from ray import ray

ray_origin = point(0, 0, -5)
wall_z = 10

wall_size = 7

canvas_pixels = 100

pixel_size = wall_size/canvas_pixels

half = wall_size/2

canv = canvas(canvas_pixels, canvas_pixels)
red = color(255, 0, 0)
shape = sphere()

for y in range(canvas_pixels):
    print('line {} of {}'.format(y+1, canvas_pixels))
    world_y = half - pixel_size * y
    for x in range(canvas_pixels):
        world_x = -half + pixel_size * x
        position = point(world_x, world_y, wall_z)
        r = ray(ray_origin, (position-ray_origin).normalize())
        xs = shape.intersect(r)
        if xs:
            canv.write_canvas(x, y, red)

canv.to_ppm(filename='ch5_test')
