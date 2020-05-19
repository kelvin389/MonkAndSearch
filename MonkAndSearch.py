size = int(input())
arr = input().split()
q = int(input())

for i in range(q):
	inp = input().split()
	qType = int(inp[0])
	x = inp[1]
	oob = False

	low, mid, high = 0, 0, len(arr)
	while (low <= high):
		mid = int((low + high) / 2)

		if mid > len(arr) - 1:
			oob = True
			break

		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		else:
			break
	
	if oob:
		print(0)
	else:
		if qType == 0:
			print(len(arr) - 1 - mid + 1)
		else:
			print(len(arr) - 1 - mid)