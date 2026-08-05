class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                nums.pop(fast)
            
            else:
                slow += 1
                fast += 1
        
        return len(nums)