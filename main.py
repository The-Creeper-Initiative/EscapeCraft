from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


# Everything in minecraft is a "voxel" - a three dimensional pixel.
# It needs to be a button so that I can detect button presses.
class Voxel(Button):
	def __init__(self, position: tuple, color = color.color(0, 1, random.uniform(0.9, 1))):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = 'white_cube',
			color = color
		)

	# This is why Voxel extends Button
	def input(self, key):
		if self.hovered:
			if key == 'right mouse down':
				voxel = Voxel(self.position + mouse.normal, color = color.color(0, 1, random.uniform(0.9, 1)))

			if key == 'left mouse down':
				destroy(self)


# I want just a cube for the walls
class Wall(Button):
	def __init__(self, position: tuple, color = color.color(0, 0, random.uniform(0.9, 1))):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = 'white_cube',
			color = color
		)

	def input(self, key):
		if self.hovered:
			if key == 'right mouse down':
				voxel = Voxel(self.position + mouse.normal, color = color.color(0, 1, random.uniform(0.9, 1)))
				

# baseplate
for z in range(15):
	for x in range(15):
		voxel = Wall((x, 0, z), color.color(0, 0, random.uniform(0.9, 1)))

# ceiling
for z in range(15):
	for x in range(15):
		voxel = Wall((x, 10, z), color.color(0, 0, random.uniform(0.9, 1)))

# ======================================================================== #
# Walls
# ======================================================================== #
for x in range(15):
	for y in range(10):
		voxel = Wall((x, y, 0), color.color(0, 0, random.uniform(0.9, 1)))

for x in range(10):
	for y in range(15):
		voxel = Wall((0, x, y), color.color(0, 0, random.uniform(0.9, 1)))

for x in range(10):
	for y in range(15):
		voxel = Wall((y, x, 14), color.color(0, 0, random.uniform(0.9, 1)))

for x in range(10):
	for y in range(15):
		voxel = Wall((14, x, y), color.color(0, 0, random.uniform(0.9, 1)))
# ======================================================================== #

player = FirstPersonController()
player.x += 12
player.z += 12


app.run()
