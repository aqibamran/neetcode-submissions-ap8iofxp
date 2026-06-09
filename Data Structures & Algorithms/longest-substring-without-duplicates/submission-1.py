class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, cur, best = -1, [], 0

        for r in range(len(s)):
            cur.append(s[r])
            print(cur)
            while len(cur) != len(set(cur)):
                l+=1
                cur.pop(0)
            best = max(best, r-l)


        return best