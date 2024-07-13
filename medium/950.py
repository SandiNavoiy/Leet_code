from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        queue = deque()
        desc_sorted_deck = sorted(deck, reverse=True)
        print(desc_sorted_deck)
        for value in desc_sorted_deck:
            queue.rotate()
            queue.appendleft(value)
            print(queue)
        return queue


deck = [17, 13, 11, 2, 3, 5, 7]
s = Solution()
print(s.deckRevealedIncreasing(deck))
