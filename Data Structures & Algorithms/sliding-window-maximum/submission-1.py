class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        i = 0
        ans = list()
        while i < len(nums)-k+1:
            wins = i+k; 
            sarry = nums[i:wins]
            ans.append(max(sarry))
            i=i+1
        return ans
