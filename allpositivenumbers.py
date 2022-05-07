nums = [12, -7, 5, 64, -14]
nums1 = [12, 14, -95, 3] 
print("Original numbers in the list: ",nums)
print("Original numbers in the list: ",nums1)
new_nums = list(filter(lambda x: x >0, nums))
new_nums1 = list(filter(lambda x: x >0, nums1))
print("Positive numbers in the list: ",new_nums)
print("Positive numbers in the list: ",new_nums1)
