class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        answer = 0

        for percentage in batteryPercentages:
            if percentage > answer:
                answer += 1

        return answer