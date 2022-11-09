import random
import string

# The Storage class is used to maintain a two-way mapping of
# long to short URLs and short to long URLs
# TODO in future: add in functionality for deleting or updating URL
# mappings as well
class Storage:
    def __init__(self):
        self.short_long = {}
        self.long_short = {}
        self.domain = "http://elieurlgenerator.com/"
    
    # Storage.find_short(long_url): Retrieve and return short URL for given long URL
    def find_short(self, long_url: str):
        if long_url in self.long_short:
            return self.long_short[long_url]
        return None
    
    # Storage.find_long(short_url): Retrieve and return full long URL for given short URL
    def find_long(self, short_url: str):
        if short_url.startswith(self.domain):
            short_url = short_url[len(self.domain):]
        if short_url in self.short_long:
            return self.short_long[short_url]
        return None
    
    # Storage.add(): Create new long URL -> short URL transformation and store mapping
    def generate(self, long_url: str) -> str:
        # short URL has already been generated for this specific URL
        # TODO in future: should we handle negligible variation in the
        # long URL passed? such as 'http://google.com' versus 'http://google.com/'
        if self.find_short(long_url) != None:
            return self.domain + self.find_short(long_url)
        
        # Generate new shortened URL extension of 10 characters and ensure it
        # does not exist yet.
        # TODO in future: research more into the best ways to generate the short
        # URLs. We do not want any collisions here ideally.
        short = ''.join(random.choices(string.ascii_lowercase, k=10))
        while self.find_long(short) != None:
            short = ''.join(random.choices(string.ascii_lowercase, k=10))
        
        # Add both mappings
        self.short_long[short] = long_url
        self.long_short[long_url] = short
        return self.domain + short
        
            
            