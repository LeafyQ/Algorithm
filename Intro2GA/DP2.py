'''
[Graduate Algorithm @galTech/ Ud401]
web page: https://gt-algorithms.com/
Content: 2.DP: Knapsack & prefix/suffix/substring Algo
Author: Rebecca
'''

# first version of knapsack DP: 0/1 problem
# argument: a list of obj with value v, weight w, and constrain C
# assumption: all the values and weights are int
# running time and space: O(nC)
def Knapsack(v,w,C):
	n = len(v)
	mat = [[0]*(n+1) for i in range(C+1)]
	print(mat)

	# the subproblem depends on the constrain
	# will finish the DP table row by row
	for c in range(1, C+1):
		for i in range(n):
			if w[i]<=c:
				mat[c][i+1] = max(v[i]+mat[c-w[i]][i], mat[c][i])
			else: # cannot fit the i-th element in the pack
				mat[c][i+1] = mat[c][i] 

	print(mat)
	return mat[-1][-1]

# ------------ simple test -------------
C = 22
v = [19,10,9,2]
w = [15,12,10,1]
print(Knapsack(v,w,C))
# --------------------------------------


# 0/1 knapsack DP extension: allow repitition
# argument: a list of obj with value v, weight w, and constrain C
# assumption: all the values and weights are int
# running time : O(nC) space: O(C)
def Knapsack_rep(v,w,C):
	n = len(v)
	DP = [0]*(C+1)

	for c in range(1,C+1):
		for i in range(n):
			if w[i]<=c and DP[c]<v[i]+DP[c-w[i]]:
				DP[c] = v[i]+DP[c-w[i]]
	print( [(i,DP[i]) for i in range(C+1)])
	return DP[-1]


# ------------ simple test -------------
C = 22
v = [13,10,9,1]
w = [15,12,10,1]
print(Knapsack_rep(v,w,C))
# --------------------------------------













