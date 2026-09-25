# nums = [3,2,4]
# target = 6

# map = {}

# def twoSum (nums, target):
#     for i in range(len(nums)):
#         needed = target - nums[i]
#         if needed in map:
#             return [map[needed], i]
#         else:
#             map[nums[i]] = i
# print(twoSum(nums=[1,2,3], target=3))


























nums = [3, 2, 4]
target = 6

map = {}
def twoSum(nums, target):
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in map:
            return [map[needed], i]
        else:
            map[nums[i]] = i
        print(map)
print(twoSum(nums, target))
