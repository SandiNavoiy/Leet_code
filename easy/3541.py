from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        """Найдите наиболее частые гласные и согласные"""

        glass = ("a", "e", "i", "o", "u")

        gl = ""
        sogl = ""
        for i in s:
            if i in glass:
                gl = gl + i
            else:
                sogl = sogl + i

        gl = Counter(gl)
        sogl = Counter(sogl)
        gl_max = ""
        gl_max_ind = 0
        sogl_max = ""
        sogl_max_ind = 0

        for k, v in gl.items():
            if v > gl_max_ind:
                gl_max = k
                gl_max_ind = v

        for k, v in sogl.items():
            if v > sogl_max_ind:
                sogl_max = k
                sogl_max_ind = v
        return gl_max_ind + sogl_max_ind


s = Solution()
print(s.maxFreqSum("successes"))
