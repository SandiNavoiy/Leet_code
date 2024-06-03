class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        ''''''
        if len(hand) % groupSize != 0:
            return False
        hand.sort()

        return hand

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

s = Solution()
print(s.isNStraightHand(hand, groupSize))