
from random import choice
from string import ascii_letters
class Codec:
    def __init__(self):
        self.name = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.name.keys():
            self.name[longUrl] = ''.join(choice(ascii_letters) for i in range(12))

        return self.name[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        for k, v in self.name.items():
            if v == shortUrl:
                return k
url = "https://leetcode.com/problems/design-tinyurl"
# Your Codec object will be instantiated and called as such:
codec = Codec()


print(codec.decode(codec.encode(url)))
