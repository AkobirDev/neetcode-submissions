class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        cum_sum = 0
        result = 0

        for num in nums:
            cum_sum += num
            result += count[cum_sum - k]
            count[cum_sum] += 1
        
        return result