import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cetxt = re.sub(r'[^a-zA-Z0-9]','',s)
        return cetxt == cetxt[::-1]
        