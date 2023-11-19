class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length*width*height
        if (volume >= 10**9 or height >= 10**4 or width >= 10**4 or length >= 10**4) and mass >=100:
            return ("Both")
        elif (volume < 10**9 or height < 10**4 or width < 10**4 or length < 10**4) and mass >=100:
            return ("Heavy")
        elif (volume >= 10**9 or height >= 10**4 or width >= 10**4 or length >= 10**4) and mass <100:
            return ("Bulky")
        else:
            return ("Neither")
length = 1000
width = 35
height = 700
mass = 300
s = Solution()
s.categorizeBox(length, width, height, mass)