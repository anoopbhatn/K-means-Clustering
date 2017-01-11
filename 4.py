# K-means clustering for 100 measurements

import random
import math
import matplotlib.pyplot as plt

points=list()
for i in range(100):
	points.append((random.randrange(1,101,1),random.randrange(1,101,1)))
px=sorted(points)
py=sorted(points,key=lambda tup: tup[1])

def distance(x,y):
	return math.sqrt((math.pow((x[0]-y[0]),2))+(math.pow((x[1]-y[1]),2)))

def maxi(p1,p2):
	if p1[2] > p2[2]:
		return p1
	else:
		return p2

def maxdist(px,n):
	m=[(0,0),(0,0),0]
	for i in range(n):
		for j in range(i+1,n):
			if distance(px[i],px[j]) > m[2]:
				m=[px[i],px[j],distance(px[i],px[j])]
	return m
def farStrip(strip,size,d):
	m=d
	for i in range(size):
		for j in range(i+1,size):
			if (strip[j][1]-strip[i][1]) > d[2] and distance(strip[i],strip[j]) > m[2]:
				m=[strip[i],strip[j],distance(strip[i],strip[j])]
	return m

def farthest(p1,p2,n):
	if n<=3:
		return maxdist(p1,n)
	mid=n/2
	pl=list()
	pr=list()
	midpoint=p1[mid]
	for i in range(len(p2)):
		if p2[i][0]>=midpoint[0]:
			pl.append(p2[i])
		else:
			pr.append(p2[i])
	left=farthest(p1,pl,mid)
	right=farthest(p1[mid:],pr,n-mid)

	d=maxi(left,right)

	strip=list()
	for i in range(len(p2)):
		if abs(p2[i][0]-midpoint[0]) > d:
			strip.append(p2[i])
	return maxi(d,farStrip(strip,len(strip),d))
print 'The points taken are :'
print px
res1=farthest(px,py,100)

c1=res1[0]
c3=res1[1]

if abs(c1[0]-c3[0]) > abs(c1[1]-c3[1]):
	c2=px[(px.index(c1)+px.index(c3))/2]
else:
	c2=px[(py.index(c1)+py.index(c3))/2]

# we have obtained 3 points

# Finding cluster to which a point belongs
def findCluster(p,c1,c2,c3):
	if (distance(p,c1) < distance(p,c2)) and (distance(p,c1) < distance(p,c3)):
		return 1 # p belongs to cluster 1
	elif (distance(p,c2) < distance(p,c1)) and (distance(p,c2) < distance(p,c3)):
		return 2 # p belongs to cluster 2
	elif (distance(p,c3) < distance(p,c1)) and (distance(p,c3) < distance(p,c2)):
		return 3 # p belongs to cluster 3

# Finding Centroid
def centroid(points):
	cx=0
	cy=0
	for i in points:
		cx+=i[0]
		cy+=i[1]
	return (cx/float(len(points)),cy/float(len(points)))

# K-means clustering
def kmeans(c1,c2,c3):
	ch1=c1
	ch2=c2
	ch3=c3
	while True:
		l1=list() # First cluster
		l2=list() # Second cluster
		l3=list() # Third cluster
		for i in range(100):
			temp=findCluster(px[i],ch1,ch2,ch3)
			if temp==1:
				l1.append(px[i])
			elif temp==2:
				l2.append(px[i])
			else:
				l3.append(px[i])
		ch1=centroid(l1)
		ch2=centroid(l2)
		ch3=centroid(l3)
		if c1==ch1 and c2==ch2 and c3==ch3:
			break
		else:
			c1=ch1
			c2=ch2
			c3=ch3
	print '\n\nThe sizes of the three shirts to be selected are : ( Chest , Height ) '
	print '\nShirt 1 : ',c1[0],' , ',c1[1]
	print '\nShirt 2 : ',c2[0],' , ',c2[1]
	print '\nShirt 3 : ',c3[0],' , ',c3[1]
	return l1,l2,l3
	
l1,l2,l3=kmeans(c1,c2,c3)

xpo=list()
ypo=list()

for i in l1:
	xpo.append(i[0])
	ypo.append(i[1])
plt.plot(xpo, ypo, 'bo')

xpo=list()
ypo=list()

for i in l2:
	xpo.append(i[0])
	ypo.append(i[1])
plt.plot(xpo, ypo, 'yo')
plt.axis([0, 100, 0, 100])

xpo=list()
ypo=list()

for i in l3:
	xpo.append(i[0])
	ypo.append(i[1])
plt.plot(xpo, ypo, 'ro')

plt.plot([c1[0],c2[0],c3[0]],[c1[1],c2[1],c3[1]],'ko')


print 'The black dots indicate the selected sizes of shirts'

plt.show()
