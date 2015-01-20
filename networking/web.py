import rss

class WebConnector:
    def __init__(self):
        self.rss_feed = rss.FeedReader()
    def get_news(self, source):
        return self.rss_feed.get_news(source)
    def get_joke(self):
        return self.rss_feed.get_joke()

