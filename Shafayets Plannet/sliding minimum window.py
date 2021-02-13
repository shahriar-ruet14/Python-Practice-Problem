import numpy as np
def brute_rmq(arr,m):
	res=[]
	for i in range(0,len(arr)-m+1):
		subarr=arr[i:i+m] #take subarray of size m, starting from index i
		res.append(min(subarr)) #append the minimum element in result
	return res
if __name__ == "__main__":
	arr  = np.random.randint(100,size = 30)
	print(len(arr))
	print(len(brute_rmq(arr,3)))
	pass

