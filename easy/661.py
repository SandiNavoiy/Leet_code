class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """"""
        # создаем матрицу
        new = [[0] * len(img[0]) for i in range(len(img))]
        # проходим по ней
        for i in range(len(img)):
            for j in range(len(img[0])):
                sss = 0
                count = 0
                # проходим по новой матрице. отсекая края. для этого ставим мин макс. и пускаем расчет
                for k in range(max(0, i - 1), min(i + 2, len(img))):
                    for m in range(max(0, j - 1), min(j + 2, len(img[0]))):
                        sss += img[k][m]
                        count += 1
                new[i][j] = sss // count
        return new


img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
s = Solution()
print(s.imageSmoother(img))
