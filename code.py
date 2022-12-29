class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        a, b = 0, 0
        for x in range(min(nums), max(nums)+1):
            a, b = b, max(count[x] * x + a, b)
        return b


# We simply build a hash map of the counts of each number, and loop through range of numbers
    
