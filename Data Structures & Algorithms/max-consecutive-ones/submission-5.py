class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = tc = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                tc+=1
            if nums[i] == 0 or i == len(nums)-1 :
                mx= max(tc,mx)
                tc=0
        return mx          