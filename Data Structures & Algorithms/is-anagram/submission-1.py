class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        notebook = {}
        for val in s:
            notebook[val] = notebook.get(val,0) +1
        
        for val in t:
            notebook[val] = notebook.get(val,0) -1
            if notebook[val] ==0:
                del notebook[val]

        if not notebook:
            return True
        return False

        