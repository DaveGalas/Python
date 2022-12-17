def twoSum(nums, target):
    temp = []

    for a in nums:
        n = nums.index(a)
        b = nums[:n] + nums[n + 1:]
        for c in b:
            if a + c == target:
                temp.append(nums.index(a))
                temp.append(nums.index(c))

    return temp

nums = [3, 3]
target = 6

print(twoSum(nums, target))