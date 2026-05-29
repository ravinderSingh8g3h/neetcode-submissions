class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chlList = list();
        for i in nums:
            if i in chlList:
                return True
            else:
                chlList.append(i)
        return False
        