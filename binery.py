
def binary_search(arr, low, high, x):
	if high >= low:

		mid = (high + low)
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1
arr = [ 2, 3, 14, 10, 40 ]
x = 1;


# Function call
result = binary_search(arr, 0, len(arr)-1, x);

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array");
print("value of x is : ", x,"and value of arr is : ",arr[3]);
print(" ")
