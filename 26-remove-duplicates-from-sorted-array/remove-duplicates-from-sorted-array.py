class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0

        for i in nums:
            if i != nums[start]:
                start += 1
                nums[start] = i
            else:
                pass
        return start+1

        