class Solution:
    def originalDigits(self, s: str) -> str:
        """"""
        digit = {}
        for i in s:
            if i not in digit:
                digit[i] = 1
            else:
                digit[i] = digit[i] + 1
        ans = ""
        if "z" in digit:
            while digit["z"]:
                ans += "0"
                digit["z"] -= 1
                digit["e"] -= 1
                digit["r"] -= 1
                digit["o"] -= 1
        if "w" in digit:
            while digit["w"]:
                ans += "2"
                digit["t"] -= 1
                digit["w"] -= 1
                digit["o"] -= 1
        if "u" in digit:
            while digit["u"]:
                ans += "4"
                digit["f"] -= 1
                digit["o"] -= 1
                digit["u"] -= 1
                digit["r"] -= 1
        if "x" in digit:
            while digit["x"]:
                ans += "6"
                digit["s"] -= 1
                digit["i"] -= 1
                digit["x"] -= 1
        if "g" in digit:
            while digit["g"]:
                ans += "8"
                digit["e"] -= 1
                digit["i"] -= 1
                digit["g"] -= 1
                digit["h"] -= 1
                digit["t"] -= 1

        if "h" in digit:
            while digit["h"]:
                ans += "3"
                digit["t"] -= 1
                digit["h"] -= 1
                digit["r"] -= 1
                digit["e"] -= 1
                digit["e"] -= 1
        if "o" in digit:
            while digit["o"]:
                ans += "1"
                digit["o"] -= 1
                digit["n"] -= 1
                digit["e"] -= 1
        if "f" in digit:
            while digit["f"]:
                ans += "5"
                digit["f"] -= 1
                digit["i"] -= 1
                digit["v"] -= 1
                digit["e"] -= 1
        if "s" in digit:
            while digit["s"]:
                ans += "7"
                digit["s"] -= 1
                digit["e"] -= 1
                digit["v"] -= 1
                digit["e"] -= 1
                digit["n"] -= 1
        if "i" in digit:
            while digit["i"]:
                ans += "9"
                digit["n"] -= 1
                digit["i"] -= 1
                digit["n"] -= 1
                digit["e"] -= 1

        t = list(ans)
        t.sort()
        rez = "".join(t)

        return rez


s = "xsi"
sol = Solution()
print(sol.originalDigits(s))
