"""
The corresponding practices in DPV 
-----------------------------------
Chapter 6: Dynamic Programming
Author: Rebecca

"""

import sys
min = -sys.maxsize -1


# run in linear time
def Max_sum(a:list):
	n = len(a)
	max_val = a[0]
	res = [a[0]]
	idx = len(a)-1
	sub = []

	for i in range(1,n):
		if res[i-1]>0 and a[i]+res[i-1]>0:
			res.append(a[i]+res[i-1])
		else:
			res.append(a[i])

		if max_val<res[-1]:
			max_val = res[-1]
			
	# backtracking
	start, end = 0,0
	while(idx>0):
		if max_val == res[idx]:
			end = idx
			while(res[idx]>0):
				idx-=1
			start = idx if end==idx else idx+1
			break
		idx-=1

	print("optimal substring: {}".format(a[start:end+1]))
	return max_val


# ----------------------------------
t1 = [-3,-2,-1]
t2 = [-5,-10,1,-4]
t3 = [-1,1,2,-3,2,-1]
t4 = [1,2,-4,2,-1,5,-3]
t5 = [5, 15, -30, 10, -5, 40, 10]
print(Max_sum(t1))
print(Max_sum(t2))
print(Max_sum(t3))
print(Max_sum(t4)) #6
print(Max_sum(t5)) 
# ----------------------------------






# ----------------------------------





# ----------------------------------









# ----------------------------------





# ----------------------------------