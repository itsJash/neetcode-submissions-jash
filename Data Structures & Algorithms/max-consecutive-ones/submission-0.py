class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        longest_length = 0
        temp = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > longest_length:
                    longest_length = count 
            else:
                count = 0
                
        return longest_length
        