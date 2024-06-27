class Solution(object):
    def isPalindrome(self,s):
        clean_text = ''.join(char for char in s if char.isalnum())
        if clean_text.lower() == clean_text[::-1].lower():
            return True
        return False


        