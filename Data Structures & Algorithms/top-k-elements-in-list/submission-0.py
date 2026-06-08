class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = {}
        top = []
        for val in nums:
            book[val] = book.get(val,0) +1
        
        for i in range(k):
            highest_val = max(book, key=book.get)
            top.append(highest_val)
            del book[highest_val]
    
        return top
            