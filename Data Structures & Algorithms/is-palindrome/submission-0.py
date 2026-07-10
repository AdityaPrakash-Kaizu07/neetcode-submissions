class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        for i in s:
            if i.isalnum():
                continue
            else :
                s=s.replace(i,"")
        d=s[::-1]
        return True if d==s else False