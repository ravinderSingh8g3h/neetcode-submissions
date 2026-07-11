class Solution:
    def reverseString(self, s: List[str]) -> None:
        r=len(s)-1
        l=0
        while l<r:
            t= s[l]
            s[l]=s[r]
            s[r] =t
            l+=1
            r-=1
        