from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted = [0] * n

        if k == 0:
            return decrypted

        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:
                for j in range(k, 0):
                    total += code[(i + j) % n]
            decrypted[i] = total
        return decrypted


code = [5, 7, 1, 4]
k = 3
s = Solution()
print(s.decrypt(code, k))
