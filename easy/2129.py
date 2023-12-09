class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """Назовите название с заглавной буквы"""
        arr = title.split()

        for i in range(len(arr)):
            arr[i] = arr[i].lower()
            if len(arr[i]) >= 3:
                arr[i] = arr[i].title()
        return " ".join(arr)


title = "capiTalIze tHe titLe"
s = Solution()
print(s.capitalizeTitle(title))
