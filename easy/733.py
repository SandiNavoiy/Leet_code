class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, newColor: int
    ) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image

        def dfc(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != originalColor:
                return

            image[x][y] = newColor

            # Recursively call dfc for neighboring cells with boundary checks
            if x + 1 < m:
                dfc(x + 1, y)
            if x - 1 >= 0:
                dfc(x - 1, y)
            if y + 1 < n:
                dfc(x, y + 1)
            if y - 1 >= 0:
                dfc(x, y - 1)

        # Start the flood fill from the initial cell
        dfc(sr, sc)

        return image


# Example usage
image = [[0, 0, 0], [0, 0, 0]]
sr = 1
sc = 0
newColor = 2
s = Solution()
print(s.floodFill(image, sr, sc, newColor))
