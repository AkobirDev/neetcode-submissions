class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if count == 0:
                max_num = num

            if num == max_num:
                count += 1
            
            else:
                count -= 1
        
        return max_num