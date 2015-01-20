import feedparser
import unicodedata

class FeedReader:
    def __init__(self):
        self.feeds = {'AP': {'top_headlines': 'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305',
                             'us': 'http://hosted2.ap.org/atom/APDEFAULT/386c25518f464186bf7a2ac026580ce7',
                             'world': 'http://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5',
                             'politics': 'http://hosted2.ap.org/atom/APDEFAULT/89ae8247abe8493fae24405546e9a1aa',
                             'business': 'http://hosted2.ap.org/atom/APDEFAULT/f70471f764144b2fab526d39972d37b3',
                             'technology': 'http://hosted2.ap.org/atom/APDEFAULT/495d344a0d10421e9baa8ee77029cfbd',
                             'sports': 'http://hosted2.ap.org/atom/APDEFAULT/347875155d53465d95cec892aeb06419',
                             'entertainment': 'http://hosted2.ap.org/atom/APDEFAULT/4e67281c3f754d0696fbfdee0f3f1469',
                             'health': 'http://hosted2.ap.org/atom/APDEFAULT/bbd825583c8542898e6fa7d440b9febc',
                             'science': 'http://hosted2.ap.org/atom/APDEFAULT/b2f0ca3a594644ee9e50a8ec4ce2d6de',
                             'strange': 'http://hosted2.ap.org/atom/APDEFAULT/aa9398e6757a46fa93ed5dea7bd3729e'},
                     'jokes': 'http://www.jokesareawesome.com/rss/random/'
                }

    def get_news(self, src):
        cnt = 1
        news = []
        source = src.split('/')[0]
        sub = src.split('/')[1]

        url = self.feeds[source][sub]

        feed = feedparser.parse(url)

        entries = feed['entries']

        for e in entries:
            news.append('Story number ' + str(cnt))
            umsg = e['summary']
            msg = unicodedata.normalize('NFKD', umsg).encode('ascii','ignore')
            news.append(msg)
            cnt += 1
        return news
            
    def get_joke(self):
        url = self.feeds['jokes']
        feed = feedparser.parse(url)
        ujoke = feed['entries'][0]['summary']
        joke = unicodedata.normalize('NFKD', ujoke).encode('ascii', 'ignore')
        return joke


