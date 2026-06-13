from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_arr=[0] * 26

        for i in range(len(s)):
            freq_arr[ord(s[i])-ord('a')] +=1
            freq_arr[ord(t[i])-ord('a')] -=1
        return all(c==0 for c in freq_arr)
        

        