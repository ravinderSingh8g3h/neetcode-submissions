class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checkstack = []
        for i in nums:
            if i in checkstack:
                checkstack.remove(i)
            else:
                checkstack.append(i)        
        return checkstack[-1]