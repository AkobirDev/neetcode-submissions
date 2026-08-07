class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        n = len(people)
        people.sort()

        left, right = 0, n - 1
        while right >= left:
            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1
            count += 1

        return count