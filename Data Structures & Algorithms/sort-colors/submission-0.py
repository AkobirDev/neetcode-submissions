class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = mid = 0
        high = n - 1

        while mid <= high:
            val = nums[mid]
            if val == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            
            elif val == 1:
                mid += 1
            
            elif val == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        