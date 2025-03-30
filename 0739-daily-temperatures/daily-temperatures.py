class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices = []
        n = len(temperatures)
        output = [0]*n

        for index in range(n):
            while indices:
                if temperatures[indices[-1]] < temperatures[index]:
                    colder = indices.pop()
                    output[colder] = index - colder
                else:
                    break
            indices.append(index)

        return output
        