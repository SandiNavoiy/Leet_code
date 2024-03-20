class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel={"a","e","i","o","u"}
        count=0
        for i in range(len(word)):
            seen_vowel=set()
            for j in range(i,len(word)):
                if word[j] in vowel:
                    seen_vowel.add(word[j])
                    if(len(seen_vowel)==5):
                        count +=1
                else:
                    break
        return count


word = "cuaieuouac"
s = Solution()
print(s.countVowelSubstrings(word))


