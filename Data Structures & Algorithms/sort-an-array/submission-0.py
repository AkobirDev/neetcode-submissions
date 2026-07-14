class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bubble_sort(nums)