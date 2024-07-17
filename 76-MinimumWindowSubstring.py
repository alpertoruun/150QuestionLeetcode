from collections import defaultdict

def minWindow(s, t):
    if t == "": return ""
    countT, window = defaultdict(int), defaultdict(int)
    for c in t:
        countT[c] += 1
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("inf")
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window[c] += 1
        
        if c in countT and window[c] == countT[c]:
            have += 1
        
        while have == need:
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    
    l, r = res
    return s[l:r+1] if resLen != float('inf') else ""
