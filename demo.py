from path_objects import *
from plot_tools import PlotTools

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