class Solution:


    def isHappy(self, n: int) -> bool:
        def sumofsqaure(n):
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            return sum
            
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sumofsqaure(n)
        return n == 1
