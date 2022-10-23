import math
V=3
t = [1,2]
a = [0.4,1]
M=2
def calc_x(V,M,a,t):
	x = [1]*(V+1)
	for n in range(1,V+1):
		sum=0
		for i in range(0,M):
			if n >= t[i]:
				sum += a[i]*t[i]*x[n-t[i]]
		x[n]=sum/n
	return x
	
def calc_P0(x):
    
	return 1/sum(x)

x=calc_x(V,M,a,t)

def calc_Pn(x,V,M,a,t):
	P = [1]*(V+1)
	P[0]=calc_P0(x)
	for n in range(1,V+1):
		sum=0
		for i in range(0,M):
			if n >= t[i]:
				sum += a[i]*t[i]*P[n-t[i]]
		P[n]=sum/n
	return P
def calc_bn(P,V,t,i=1):
	sum=0
	for n in range(V-t[i-1]+1,V+1):
		sum+=P[n]
	return sum

def calc_all(V,t,a,M):

    x=calc_x(V,M,a,t)
    print(x)

    P=calc_Pn(x,V,M,a,t)
    print(P)

    B=[]
    for i in range(1,M+1):
        b1=calc_bn(P,V,t,i)
        B.append(b1)
    print(B)

calc_all(V,t,a,M)