


class LinkQuence:
    def __init__(self,visited=[],unVisited=[]):
        self.visited = visited
        self.unVisited = unVisited
    def getVisitedUrl(self):
        self.visited
    def getUnvisitedUrl(self):
        self.unVisited
    def addVisitedUrl(self,url):
        self.visited.append(url)
    def removeVisitedUrl(self,url):
        self.visited.remove(url)

    #pop一个未访问的url
    def popUnvisitedUrl(self):
        try:
            return self.unVisited.pop()
        except Exception as e:
            print(e)
            return None
    #保证每个url只被访问一次
    def addUnvisitedUrl(self,url):
        if url!='' and url not in self.visited and url not in self.unVisited:
            self.unVisited.append(url)

    def getVisitedUrlCount(self):
        return len(self.visited)
    def getUnvisitedUrlCount(self):
        return len(self.unVisited)
    #判断是否有未访问的url
    def hasUnVisitedUrl(self):
        return len(self.unVisited)==0


