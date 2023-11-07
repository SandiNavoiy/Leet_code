class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """Переворот изображения"""
        new_image = []
        new_image1 = []
        for i in image:
            new_image.append(i[::-1])
        for i in new_image:
            temp = []
            for j in i:
                if j == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            new_image1.append(temp)

        return new_image1


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
s = Solution()
print(s.flipAndInvertImage(image))
# [[0,1,1],[1,0,1],[0,0,0]]
# [[1,0,0],[0,1,0],[1 ,1,1]]
