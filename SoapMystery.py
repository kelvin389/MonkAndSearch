numSoaps = int(input())
arr = list(map(int, input().split()))
arr.sort()
q = int(input())

for i in range(q):
	m = int(input())

	low, mid = 0, 0
	high = len(arr) - 1

	while low <= high:
		mid = int((low + high) / 2)

		if arr[mid] < m:
			low = mid + 1
		else:
			high = mid - 1
	
	mid -= 1
	while mid < len(arr) - 1 and arr[mid + 1] < m:
		mid += 1
		
	print(mid + 1)