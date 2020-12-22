from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


block_pick = 1


# Everything in minecraft is a "voxel" - a three dimensional pixel.
# It needs to be a button so that I can detect button presses.
class Voxel(Button):
	def __init__(self, position: tuple):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = 'white_cube',
			color = color.color(0, 0, random.uniform(0.9, 1))
		)

	# This is why Voxel extends Button
	def input(self, key):
		if self.hovered:
			if key == 'right mouse down':
				voxel = Voxel(self.position + mouse.normal)
			if key == 'left mouse down':
				destroy(self)


for z in range(20):
	for x in range(20):
		voxel = Voxel((x, 0, z))


player = FirstPersonController()


def update():
	global block_pick
	 
	if held_keys[1]: block_pick = 1
	if held_keys[2]: block_pick = 2
	if held_keys[3]: block_pick = 3


app.run()
