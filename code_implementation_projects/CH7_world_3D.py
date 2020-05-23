from sphere import sphere
from matrix_transformations import scaling, translation, x_rotation, y_rotation, z_rotation, view_transform
from canvas_color import color
from math import  pi
from world import world
from camera import camera
from material import material, point_light
from bases import point, vector


floor = sphere(transform_within=scaling(10, 0.1, 10))
floor.set_transform(scaling(10, 0.01, 10))
floor.material.colour = color(1, 0.9, 0.9)
floor.material.specular = 0

left_wall = sphere(set_material=floor.material)
MAT = translation(0, 0, 5) * y_rotation(-pi/4) * x_rotation(pi/2) * scaling(10, 0.01, 10)
left_wall.set_transform(MAT)

right_wall = sphere(set_material=floor.material)
MAT2 = translation(0, 0, 5) * y_rotation(pi/4) * x_rotation(pi/2) * scaling(10, 0.01, 10)
right_wall.set_transform(MAT2)

middle = sphere()
middle.set_transform(translation(-0.5, 1, 0.5))
middle.material.colour = color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = sphere()
right.set_transform(translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5))
right.material.colour = color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3

left = sphere()
left.set_transform(translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33))
left.material.colour = color(1, 0.8, 0.1)
left.material.diffuse = 0.7
left.material.specular = 0.3


source = point_light(point(-10, 10, -10), color(1, 1, 1))

w = world(object=[middle, left, right, floor, left_wall, right_wall])
w.set_light(source)

c = camera(200, 100, pi/3)

FROM = point(0, 1.5, -5)
TO = point(0, 1, 0)
UP = vector(0, 1, 0)
data = view_transform(FROM, TO, UP)
c.Set_Transform(data)

IMAGE = c.render(w)
IMAGE.to_ppm(filename='pls')
