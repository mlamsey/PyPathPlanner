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
	def __init__(self, moves=[]):
		self.moves = moves

class Segment:
	def __init__(self, contours=[], segment_type=None):
		self.contours = contours
		self.segment_type = segment_type

class Part:
	def __init__(self, segments=[Segment()], segment_manifest=None):
		self.segments = segments
		self.segment_manifest = segment_manifest

if __name__ == '__main__':
	print("path_objects::main(): please do not run this file!")
