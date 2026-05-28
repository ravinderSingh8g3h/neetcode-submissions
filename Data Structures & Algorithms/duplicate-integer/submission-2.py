class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chlList = list();
        for i in range(0,len(nums)):
            if nums[i] in chlList:
                return True
            else:
                chlList.append(nums[i])
        return False
        