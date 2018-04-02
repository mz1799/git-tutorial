import numpy as np

g = np.matrix([[-1,-2,-1],[0,0,0],[1,2,1]])
g.astype('float64')
g = g/4.0
k = np.matrix([[67,56,89],[76,85,23],[53,255,98]])
m=1
n=1
s=np.zeros((1,9))
i=0
for u in xrange(-1,2):
	
	for v in xrange(-1,2):
		s[0,i] = k[m-u,n-v]*g[u+1,v+1]
		i = i+1
		
		
		print i
		#print v
		#print u
