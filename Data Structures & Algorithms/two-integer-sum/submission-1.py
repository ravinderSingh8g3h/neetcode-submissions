class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            # checking complement
            comp = target-nums[i]
            if comp in dict:
                return  [dict.get(comp),i]
            # storing value and index
            dict[nums[i]] = i
            




        