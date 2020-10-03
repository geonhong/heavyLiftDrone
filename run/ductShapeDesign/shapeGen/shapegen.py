#!/usr/bin/env python3

from math import sqrt, cos, sin, asin, acos, atan, atan2, radians, degrees, pi

def sqr(s):
	return s*s

def mag(s):
	return sqrt(sqr(s))

def bound(s, low, upp):
	return min( max(s, low), upp)

def func1(xl, yl, r, x):
	return (yl - sqrt(sqr(r)-sqr(x-xl)))/sqr(x)

def func2(xl, r, x):
	return (x-xl)/(2*x*sqrt(sqr(r)-sqr(x-xl)))

xl = 0.1
yl = 0.025
r  = 0.01
xte = -0.1
yte = 0.005
yo = 0.025

ptList = [[xte, 0.0]]

#- inner lip part
x = xl
dx = 0.001

xhist = []
shist = []

it = 1

while True:
	s = func1(xl, yl, r, x) - func2(xl, r, x)
	shist.append(s)
	xhist.append(x)

	#print( xhist[-1], shist[-1], end=' ' )

	if it > 1:
		dsdx = (shist[-1]-shist[-2])/(xhist[-1]-xhist[-2])
		sect = shist[-1] - dsdx*xhist[-1]
		xnew = -sect/dsdx
		#print(dsdx, sect, xnew)
		x = xnew
	else:
		x += dx
		#print('')

	it += 1

	if it>100 or mag(s)<1e-8:
		break

a = func1(xl, yl, r, x)

xsinn = x
ysinn = a*sqr(x)

#print(xsinn, ysinn)

#print('==========')
#print(' inner')

# lip inner part
for i in range(1, 11):
	frac = float(i)/10.0

	x = frac*xsinn
	y = a*sqr(x)

	if x>xsinn:
		break

	#print(x, y)

	ptList.append([x, y])

ptList.append([xsinn, ysinn])


# find outer intersection point
#   outer line: y = (ysect-yte)/(xsect-xte)*x + d
#				dy/dx = (ysect-yte)/(xsect-xte)
#   lip circle: y = yl + sqrt( sqr(r) - sqr(x-xl) )
#				dy/dx = - (x-xl)/(y-yl)
#print('==========')

dx = xl-xte
dy = yl-yte
tht0 = atan(dy/dx)
tht1 = asin(r/sqrt(sqr(dx)+sqr(dy)))
tht2 = 0.5*pi-tht1

#print(degrees(tht0), degrees(tht1), degrees(tht2))

xsout = xl - r*cos(tht2-tht1)
ysout = yl + r*sin(tht2-tht1)

#print('outer line intersects at ', xsout, ysout)

#print(x, y)

# lip circle
thts = atan((ysinn-yl)/(xsinn-xl)) 
thte = atan2((ysout-yl),(xsout-xl))

#print('circle part between: ', degrees(thts), degrees(thte))

tht = -pi
dtht = radians(10.0)

#print('==========')
#print(' circle')
while tht < pi:
	if tht>=thts and tht<=thte:
		x = xl + r*cos(tht)
		y = yl + r*sin(tht)

		#print(x, y)

		ptList.append([x, y])
	
	tht += dtht

# lip outer part
#print('==========')
#print(' outer')

ptList.append([xsout, ysout])
ptList.append([xte, yte])

for pt in ptList:
	print(pt[0], pt[1])
