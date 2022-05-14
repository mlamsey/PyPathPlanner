import numpy as np
from plot_tools import PlotTools

class Waypoint:
	def __init__(self, pos=np.array([0., 0., 0.]), rotmat=np.eye(3)):
		self.pos = pos
		self.rotmat = rotmat
class Move:
	def __init__(self, point0=Waypoint(), point1=Waypoint(), move_type=None):
		self.point0 = point0
		self.point1 = point1
		self.move_type = move_type

class Contour:
	def __init__(self, moves=[Move()]):
		self.moves = moves

class Segment:
	def __init__(self, contours=[Contour()], segment_type=None):
		self.contours = contours
		self.segment_type = segment_type

class Part:
	def __init__(self, segments=[Segment()], segment_manifest=None):
		self.segments = segments
		self.segment_manifest = segment_manifest

if __name__ == '__main__':
	# print("path_objects::main(): please do not run this file!")
	print("path_objects::main(): generating test wall")

	# parameters
	n_layers = 10
	layer_length = 25.4 * 6 # 6in -> mm
	layer_height = 2 # mm

	# object
	part = Part()

	# build shitty wall
	for i in range(n_layers):
		z = i * layer_height
		p0 = Waypoint(np.array([0., 0., z]))
		p1 = Waypoint(np.array([layer_length, 0., z]))
		move = Move(p0, p1)
		contour = Contour([move])
		part.segments[0].contours.append(contour)

	# plot demo
	pt = PlotTools()
	pt.PlotPart(part)
