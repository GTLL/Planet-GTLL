#!/usr/bin/env python

import config
from models import Feed

class Crawler(object):

    def __init__(self):
        self.feeds = []
        cfg = config.config()
        for section in cfg.sections():
            if section == "META":
                continue
            d = {}
            d.update(cfg.items(section))
            print d
            feed = Feed(id=section, **d)
            self.feeds.append(feed)

    def crawl(self):
        for source in self.feeds:
            print "Crawling", source
            source.crawl()


if __name__ == '__main__':
    crawler = Crawler()
    crawler.crawl()
