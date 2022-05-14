import numpy as np
import algorithms.contour_algorithms as ca

def TranslateSegment(segment, new_pos):
	for i in range(len(segment.contours)):
		contour = segment.contours[i]
		new_contour = ca.TranslateContour(contour, new_pos)
		
		if new_contour is not None:
			segment.contours[i] = new_contour

	return segment