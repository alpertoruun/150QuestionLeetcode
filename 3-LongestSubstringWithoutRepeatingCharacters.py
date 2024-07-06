def lengthOfLongestSubstring(s):
    n=len(s)
    l=0
    charSet=set()
    res=0
    for r in range(n):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res=max(res,r-l+1)
        return res





