class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        total_skill = skill[0] + skill[-1]
        total = 0
        while l < r:
            if skill[l] + skill[r] != total_skill:
                return -1
            else:
                total += skill[l] * skill[r]

            l += 1
            r -= 1
        return total