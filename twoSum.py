class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = 0
        for index_1,number_1 in enumerate(nums):
            for index_2 in range(index_1+1,len(nums)):
                if ((nums[index_2] + number_1) == target):
                    return [index_1,index_2]
            
ret = Solution().twoSum([2,7,11,15], 9)