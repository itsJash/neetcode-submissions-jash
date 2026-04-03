class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # final_map = {}
        # for n,i in enumerate(s):
        #     final_map[i] = n

        # return t in final_map

     
        return sorted(t) == sorted(s)

        