'''
[Graduate Algorithm @galTech]
web page: https://gt-algorithms.com/
Content: 1.DP
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







