'''
Data structures for storing autotrace-compatible tongue contours
'''

import os

class Point(object):

	def __init__(self, coordinate, x, y):
		self.coordinate = float(coordinate) if coordinate else -1
		self.x = float(x) if x else -1
		self.y = float(y) if y else -1
	def __repr__(self):
		return "coord:\t{0}\nx:\t{1}\ny:\t{2}".format(self.coordinate, self.x, self.y)


class Contour(object):

	def __init__(self, data):
		self.points = [Point(*d) for d in data]
		self.length = len(self.points)
		self.valid = [p for p in self.points if p.coordinate != -1]

	# alternative constructor-like thing for constructing a Point from a *.traced.txt file
	@classmethod
	def fromfilename(cls, fname):
		return cls([p.strip().split("\t") for p in open(fname, 'r').readlines()])

	def __repr__(self):
		return "Contour with {0} points ({1} valid)".format(self.length, len(self.valid))

if __name__ == "__main__":
	contours = [Contour.fromfilename(f) for f in os.listdir(os.path.expanduser("~/github/APIL-stuff/APIL_data/preprocessing/train/HS_diverse_800_50/traces")) if f.endswith("traced.txt")] #Contour("20110826JF_0818.jpg.ghp.traced.txt")
