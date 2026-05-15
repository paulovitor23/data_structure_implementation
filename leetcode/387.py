from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx,ch in enumerate(s):
            if not d.get():
                d[ch] = [idx, 1]
            else:
                d[ch][1] += 1
            
        for k,v in d.items():
            if v[1] == 1:
                return v[0]
        
        return -1