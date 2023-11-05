class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        """Максимальное количество слов, найденных в предложениях"""
        ma = 0
        for i in sentences:
            if i.count(" ") > ma:
                ma = i.count(" ")



        return ma + 1

sentences = ["Алиса и Боб любят литкод", "Я тоже так думаю", "Это здорово, большое спасибо" ]

s = Solution()
print(s.mostWordsFound(sentences))


