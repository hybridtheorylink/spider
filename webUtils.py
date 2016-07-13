import urllib.request
from lxml import etree
import socket
import Constant

# 获取网页源码
def getPageNodes(url,timeout=5,encoding=None):
    try:
        socket.setdefaulttimeout(timeout)
        res = urllib.request.urlopen(url, data=None, timeout=Constant.REQ_TIME_OUT)
        html = res.read()
        nodes = etree.HTML(html)
        return nodes
    except Exception as e:
        print(e)
        return None

#获取源码中得超链接
def getHyperLinks(nodes):
    if(nodes is not None):return nodes.xpath('//a/@href')
    return []
#为./ 与 / 添加parent路径
def adjustUrl(parent,url):
    if(url=='' or url is None):return None
    if(url.startswith('http')):return url
    if(url.startswith('./')):
        urlparse = urllib.parse.urlparse(parent)
        path = urlparse.path
        if(path.endswith('/')):path = path[0:len(path)-1]
        return urlparse.scheme + '://' + urlparse.netloc + path + url[1:len(url)]
    if(url.startswith('/')):
        urlparse = urllib.parse.urlparse(parent)
        return urlparse.scheme+'://'+urlparse.netloc+url
    return None



