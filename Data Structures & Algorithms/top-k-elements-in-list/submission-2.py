class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        result = []
        for _ in range(k):
            max_freq = 0
            max_val = None

            for key, val in freq.items():
                if val > max_freq:
                    max_freq = val
                    max_val = key
                
            result.append(max_val)
            
            del freq[max_val]
        
        return result