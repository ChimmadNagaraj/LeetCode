#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def twoSum(nums, target):
        d = dict()
        for i in range (len(nums)):
            if (target-nums[i]) in d:
                return [d[target-nums[i]],i]
            if nums[i] not in d:
                d[nums[i]]=i

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums,target)
print(result)
