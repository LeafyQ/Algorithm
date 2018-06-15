'''
[Graduate Algorithm @galTech/ Ud401]
web page: https://gt-algorithms.com/
Content: 1.DP: FIB, LIS, LCS
Author: Rebecca
'''

#buttom-up DP version of fib
def fib(n):
	d = [0,1]
	for i in range(2,n):
		d.append(d[i-1] + d[i-2])
	return d[n-1]

# ------------ simple test -------------
print(fib(2))
print(fib(10))
# --------------------------------------


#Longest Increasing Subsequence(LIS)
# definition of Subsequence -- allow skip elements
def LIS(a:list):
	n = len(a)
	max_l = 1
	lis = [1]*n
	for i in range(1,n):
		for j in range(0,i):
			if a[i]>a[j] and lis[i]< lis[j]+1:
				lis[i] = lis[j]+1
		if max_l<lis[i]:
			max_l = lis[i]
	return max_l


# ------------ simple test -------------
l = [7,11,-5,-2,15,1,16,6,7,11,8,9,0]
print(LIS(l))
print(LIS(l[:1]))
# --------------------------------------


#LCS: longest common subsequence
# Naive: running time O(mn), space O(mn)
# additional information allowing tracking subsequence
"""
add-on info: add additional row and col as initial condition L(0,j) == L(i,0) == 0
			 would make the generation easier. In this situation, should return mat[m][n]
"""

def LCS(a,b):
	m,n  = len(a), len(b)
	mat = [[0]*n for i in range(m)]
	for j in range(n):
		if a[0]==b[j] or (j>0 and mat[0][j-1]>0):
			mat[0][j] = 1
			
	for i in range(m):
		if a[i]==b[0] or (i>0 and mat[i-1][0]>0):
			mat[i][0] = 1

	for i in range(1,m):
		for j in range(1,n):
			if a[i]==b[j]:
				mat[i][j] = mat[i-1][j-1] + 1
			else:
				mat[i][j] = max(mat[i-1][j],mat[i][j-1])
	#print(mat)
	return mat[m-1][n-1]#, mat

# ------------ simple test -------------
a,b = 'bbb', 'bb' 
print('The LCS of {} and {}: {}'.format(a,b,LCS(a,b)))

a,b = 'bbb', 'bbbb' 
print('The LCS of {} and {}: {}'.format(a,b,LCS(a,b)))

a,b = 'Rebecca', 'bbba' 
print('The LCS of {} and {}: {}'.format(a,b,LCS(a,b)))

a,b = 'abba', 'aba' 
print('The LCS of {} and {}: {}'.format(a,b,LCS(a,b)))

# --------------------------------------


#LCS: longest common subsequence
# space optimization: O(min(n,m))
def LCS_opt(a,b):
	m,n  = len(a), len(b)
	if(m==0 or n==0):
		return 0
	if(m<n):
		a,b = b,a
		m,n = n,m
	curr,prev = [0]*n,[0]*n
	for j in range(n):
		if a[0]==b[j] or (j>0 and prev[j-1]>0):
			prev[j] = 1
	for i in range(m):
		if a[i] == b[0] or prev[0]>0:
			curr[0] = 1
		for j in range(1,n):
			if a[i]==b[j]:
				curr[j] = prev[j-1]+1
			else:
				curr[j] = max(curr[j-1],prev[j])
		prev = curr
		curr = [0]*n
	return prev[-1]

# ------------ simple test -------------
a,b = 'bbb', 'bb' 
print('The LCS of {} and {}: {}'.format(a,b,LCS_opt(a,b)))

a,b = 'bbb', 'bbbb' 
print('The LCS of {} and {}: {}'.format(a,b,LCS_opt(a,b)))

a,b = 'Rebecca', 'bbba' 
print('The LCS of {} and {}: {}'.format(a,b,LCS_opt(a,b)))

a,b = 'abba', 'aba' 
print('The LCS of {} and {}: {}'.format(a,b,LCS_opt(a,b)))

# --------------------------------------