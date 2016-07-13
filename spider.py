import linkQuence
import webUtils
import strUtils
import logger
class Spider:
    #初始化对象
    def __init__(self,startUrls=[],netlocs=[],allows=[],callback=None):
        self.startUrls = startUrls
        self.netlocs = netlocs
        self.allows = allows
        #设置开始url
        quence = linkQuence.LinkQuence(unVisited=startUrls)
        self.linkQuence = quence
        self.callback = callback

    #设置回调函数
    def caller(self,url=None,nodes=[]):
        self.callback(url,nodes)
    def setCallback(self,callback):
        self.callback = callback

    # 判断链接是否需要抓取
    def checkUrl(self,url):
        if (url is None or url == ''):return False
        #匹配爬虫url
        if (self.allows is not None and not strUtils.matchs(url, self.allows)): return False
        if (self.netlocs is not None and url.find(self.netlocs) < 0 ): return False
        if(not url.startswith('http')):return False
        return True
    #开始抓取方法
    def startCrawl(self):
        while not self.linkQuence.hasUnVisitedUrl():
            allLinks = []
            while not self.linkQuence.hasUnVisitedUrl():
                #队头url出队列
                visitUrl = self.linkQuence.popUnvisitedUrl()
                print('pop out one url:'+visitUrl)
                #判断链接是否有效
                if(not self.checkUrl(visitUrl)):continue

                nodes = webUtils.getPageNodes(visitUrl)
                if(nodes is None):continue
                #添加超链接
                links = webUtils.getHyperLinks(nodes)
                for link in links:
                    #统一调整url格式
                    link = webUtils.adjustUrl(visitUrl,link)
                    if(link is not None):allLinks.append(link)
                print('Get %d new links'%len(links))
                self.linkQuence.addVisitedUrl(visitUrl)
                logger.log(visitUrl)
                #调用回调函数
                self.caller(visitUrl,nodes)
            # 添加超链接到未访问队列中
            for link in allLinks:
                self.linkQuence.addUnvisitedUrl(link)
            if(not self.linkQuence.hasUnVisitedUrl()):
                print('crawl end')







