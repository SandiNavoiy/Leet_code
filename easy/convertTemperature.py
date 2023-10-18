class Solution(object):
    """Класс конвертации температур"""
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        if 0 <= celsius <= 1000:
            return [round((celsius + 273.15), 5), round((celsius * 1.80 + 32.00), 5)]
        else:
            return print("celsius is 0 <= and <= 1000")



solution = Solution()
convert_temper = solution.convertTemperature(155151515)
print(convert_temper)