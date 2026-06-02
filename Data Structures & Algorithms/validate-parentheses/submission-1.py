class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :
            return False
        dic = { '{':'}','[':']' ,'(':')'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif not stack or dic[stack.pop()] != i:
                return False
        return len(stack)==0


        