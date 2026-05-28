class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        ans = list()
        for i in range(0,len(nums)):
            # checking complement
            comp = target-nums[i]
            if comp in dict:
                ans.extend([dict.get(comp),i])
                break
            # storing value and index
            dict[nums[i]] = i
        print(dict)
        return ans
            




        