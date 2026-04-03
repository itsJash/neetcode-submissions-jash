class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and i !=j:
                    # output.append(i)
                    # output.append(j)
                    return [i,j]
            