import numpy as np
import algorithms.segment_algorithms as sa

def TranslatePartToPoint(part, new_center_pos):
	for i in range(len(part.segments)):
		segment = part.segments[i]
		new_segment = sa.TranslateSegment(segment, new_center_pos)
		
		if new_segment is not None:
			part.segments[i] = new_segment

	return part
