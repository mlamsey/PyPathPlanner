import matplotlib.pyplot as plt

class PlotTools:
	def __init__(self):
		pass

	def PlotPart(self, part, figure_ref=plt.figure()):
		print("I'm plotting!")
		f = figure_ref
		a = f.add_subplot(111, projection='3d')

		for segment in part.segments:
			self.PlotSegment(segment, a)

		self.DefaultConfig(a)
		plt.show()

	def PlotSegment(self, segment, axes_ref):
		for contour in segment.contours:
			self.PlotContour(contour, axes_ref)

	def PlotContour(self, contour, axes_ref):
		for move in contour.moves:
			self.PlotMove(move, axes_ref)

	def PlotMove(self, move, axes_ref):
		x = [move.point0.pos[0], move.point1.pos[0]]
		y = [move.point0.pos[1], move.point1.pos[1]]
		z = [move.point0.pos[2], move.point1.pos[2]]

		axes_ref.plot(x, y, z, 'black')

	def DefaultConfig(self, axes_ref):
		axes_ref.set_xlabel("X (mm)")
		axes_ref.set_ylabel("Y (mm)")
		axes_ref.set_zlabel("Z (mm)")
		axes_ref.grid()
