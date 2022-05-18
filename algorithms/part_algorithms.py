import numpy as np
import algorithms.segment_algorithms as sa
import algorithms.contour_algorithms as ca

def TranslatePartToPoint(part, new_center_pos):
	center_of_first_contour = ca.FindContourCentroid(part.segments[0].contours[0])
	new_pos = new_center_pos - center_of_first_contour

	for i in range(len(part.segments)):
		segment = part.segments[i]
		new_segment = sa.TranslateSegment(segment, new_pos)
		
		if new_segment is not None:
			part.segments[i] = new_segment

	return part
