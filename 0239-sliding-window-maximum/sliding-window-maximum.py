class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deck = deque()
        output = []

        for i in range(k):
            addition = nums[i]
            while deck and addition > nums[deck[-1]]:
                deck.pop()
            deck.append(i)

        output.append(nums[deck[0]])
        print(deck)

        for i in range(k, len(nums)):
            addition = nums[i]
            while deck and addition > nums[deck[-1]]:
                deck.pop()
            deck.append(i)
            while deck[0] <= i - k:
                deck.popleft()
            output.append(nums[deck[0]])
        print(deck)
        return output
            



            
        
        