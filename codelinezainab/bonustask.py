def running_sum(nums):
    if not nums:
        return []

    running_sum_list = [nums[0]]

    for i in range(1, len(nums)):
        running_sum_list.append(running_sum_list[-1] + nums[i])

    return running_sum_list

# Example usage:
nums1 = [1, 2, 3, 4]
result1 = running_sum(nums1)
print(result1)  # Output: [1, 3, 6, 10]

nums2 = [1, 1, 1, 1, 1]
result2 = running_sum(nums2)
print(result2)  # Output: [1, 2, 3, 4, 5]

nums3 = [3, 1, 2, 10, 1]
result3 = running_sum(nums3)
print(result3)  # Output: [3, 4, 6, 16, 17]
