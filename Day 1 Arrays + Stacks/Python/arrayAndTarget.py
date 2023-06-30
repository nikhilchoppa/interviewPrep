# Q: Given a set of numbers, find a pair of numbers that add up to a certain target. 
# Ex: given [1,2,3,9] and a target of 10, identify that 1 and 9 add up to 10.

# Brute Force Approach (O(n^2))

def find_pair_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])
    return None

print(find_pair_brute([1,2,3,9], 10)) # Returns: (1,9)

#----------------------------------------------------------------------------

# Using Sorting and Two Pointers Approach (O(nlogn))

def find_pair_sort(nums, target):
    nums.sort()
    left, right = 0, len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (nums[left], nums[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1      
    return None
print(find_pair_sort([1,2,3,9], 10)) 

#----------------------------------------------------------------------------

# Using a Hsh Map (O(n))

def find_pair_hash(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return (target - num, num)
        num_map[num] = i
    return None

print(find_pair_hash([1,2,3,9], 10))
