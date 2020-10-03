#!/usr/bin/env python3

class point:
	
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def __add__(self, pt):
		self.x += pt.x
		self.y += pt.y
		self.z += pt.z
	
	def __sub__(self, pt):
		self.x -= pt.x
		self.y -= pt.y
		self.z -= pt.z

class lineseg:
	
	def __init__(self, pt1, pt2):
		self.slp = (pt2.y-pt1.y)/(pt2.x-pt1.x)
		self.sct = pt1.y - self.slp*pt1.x

	def __str__(self):
		return 'y = ' + str(self.slp) + ' x + ' + str(self.sct)

def sect(l1, l2):
	x = (l2.sct - l1.sct)/(l1.slp - l2.slp)
	y = l1.slp*x + l1.sct

	return x, y


Llip = 0.1
Dlip = 0.37
Dprop = 0.35

ndiv = 6

for i in range(1, ndiv+1):

	frac = float(i)/float(ndiv)
	x = frac*(Dlip-Dprop) + Dprop
	y = frac*Llip

	pts1 = point(Dprop, y, 0.0)
	pts2 = point(x, Llip, 0.0)

	lseg1 = lineseg(pts1, pts2)

	frac = float(i+1)/float(ndiv)
	x = frac*(Dlip-Dprop) + Dprop
	y = frac*Llip

	pts1 = point(Dprop, y, 0.0)
	pts2 = point(x, Llip, 0.0)

	lseg2 = lineseg(pts1, pts2)

	x, y = sect(lseg1, lseg2)

	print(i, x, y)

