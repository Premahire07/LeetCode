class Solution(object):
    def twoSum(self, nums, target):
        add = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                add = nums[i] + nums[j]
                if add == target:
                    return [i,j]
                else:
                    add = 0


                