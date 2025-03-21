class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = [0]*26
        count2 = [0]*26

        for index in range(len(s1)):
            count1 [ord(s1[index]) - ord('a')] += 1
            count2 [ord(s2[index]) - ord('a')] += 1
        if tuple(count1) == tuple(count2):
            return True
        left = 0
        for index in range(len(s1), len(s2)):
            count2[ord(s2[index]) - ord('a')] += 1
            count2[ord(s2[left]) - ord('a')] -= 1
            if tuple(count1) == tuple(count2):
                return True
            left += 1

        return False

            

        