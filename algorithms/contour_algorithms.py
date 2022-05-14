import numpy as np
import algorithms.move_algorithms as ma

def TranslateContour(contour, new_pos):
	for i in range(len(contour.moves)):
		move = contour.moves[i]
		new_move = ma.TranslateMove(move, new_pos)

		if new_move is not None:
			contour.moves[i] = new_move

	return contour