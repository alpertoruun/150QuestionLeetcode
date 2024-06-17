class Solution(object):
    def strStr(self, haystack, needle):
        sayac=0
        i=0
        j=0
        first_index=0
        while i < len(haystack):
            if sayac !=0 and haystack[i] != needle[j]:
                sayac=0
                j=0
                i=first_index+1
            if haystack[i] == needle[j]:
                if sayac==0:
                    first_index=i
                sayac +=1
                j +=1
            i +=1
            if sayac == len(needle):
                return i-len(needle)
        return -1
