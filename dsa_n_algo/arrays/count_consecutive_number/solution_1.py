nums = [1, 1, 0, 1, 1, 1, 0]

count = 0
max_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
    else:
        count = 0
    
    if count > 0 and count > max_count:
        max_count += 1

print(max_count)