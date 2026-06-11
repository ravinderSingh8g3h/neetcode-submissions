class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        ans = []
        l=0
        for i in range(0,len(nums)):
            #maintaing decreasing deque
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            # keeping window intact and removing elemants out of window
            if l > d[0]:
                d.popleft()       
            #adding ans
            if i+1 >=k:
                ans.append(nums[d[0]])
                l+=1

        return ans
    