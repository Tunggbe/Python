nums = [-1,0,3,5,9,12]
target = 9

def binary_find(nums, target):
	right_inx = len(nums)-1
	left_idx = 0
	while left_idx <= right_inx:
		mid_idx = left_idx + (right_inx + left_idx) // 2
		mid = nums[mid_idx]
		if nums[mid_idx] == target:
			return mid_idx
		elif target < nums[mid_idx]:
			right_inx = mid_idx - 1
		elif target > nums[mid_idx]:
			left_idx = mid_idx - 1
	return -1

print(binary_find(nums,target))



