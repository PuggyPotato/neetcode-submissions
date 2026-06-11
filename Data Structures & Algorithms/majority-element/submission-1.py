class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        book = {}
        for val in nums:
            book[val] = book.get(val,0) +1

        return max(book, key=book.get)