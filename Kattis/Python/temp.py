def bin_search(low,high,val):
	if low == high:
		return -1
	mid = (low+high)//2
	if val == mid:
		return val
	if mid > val:
		return bin_search(mid+1,high,val)
	return bin_search(low,mid-1,val)
