class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current = 0

                while num + current in nums_set:
                    current += 1
                
                result = max(result, current)

        return result
            


"""
[2,20,4,10,3,4,5]

result = 0

"""