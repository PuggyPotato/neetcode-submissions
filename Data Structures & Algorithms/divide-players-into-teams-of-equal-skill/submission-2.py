class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        skill_benchmark = skill[0] + skill[-1]
        total = 0

        while l < r:
            if skill[l] + skill[r] != skill_benchmark:
                return -1
            total += skill[l] * skill[r]

            l += 1
            r -= 1
        return total