# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

class Codec:
    urlMapping = dict()
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        shortUrl = (f'http://tinyurl.com/{x}')
        self.urlMapping[x] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urlMapping[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
codec.decode(codec.encode(url))
