import numpy as np
import algorithms.move_algorithms as ma

def GetContourWaypointVectors(contour):
	n_points = len(contour.moves) + 1 # assumes continuous points...
	pos = np.zeros([n_points, 3])

	for i in range(n_points - 1):
		move = contour.moves[i]
		pos[i, :] = move.point0.pos

	pos[-1, :] = contour.moves[-1].point1.pos
	print(pos)
	x = pos[:, 0]
	y = pos[:, 1]
	z = pos[:, 2]

	return x, y, z

def FindContourCentroid(contour):
	pass

def TranslateContour(contour, new_pos):
	for i in range(len(contour.moves)):
		move = contour.moves[i]
		new_move = ma.TranslateMove(move, new_pos)

		if new_move is not None:
			contour.moves[i] = new_move

	return contour