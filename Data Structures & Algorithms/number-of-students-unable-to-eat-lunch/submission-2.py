class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ptr1 = 0
        while ptr1 < len(students):
            if students[ptr1] == sandwiches[0]:
                students.pop(ptr1)
                sandwiches.pop(0)
                ptr1 = 0
            else:
                ptr1 += 1

        return len(students)