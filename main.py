from spider import Spider
import _thread
import imageUtils
import strUtils
from lxml import etree
import webUtils

def downloadImg(url,nodes):
    imgs = nodes.xpath('//img/@src')
    for img in imgs:
        if(webUtils.adjustUrl(url,img) is None):continue
        try:
            _thread.start_new_thread(imageUtils.downloadImage,(img,))
        except Exception as e:
            print(e)

startUrsl = ['https://movie.douban.com/subject/3569910/']
netlocs = 'douban.com'
allows = ['.*douban.*']


spider1 = Spider(startUrls=startUrsl,netlocs=netlocs,allows=allows,callback=downloadImg)

spider1.startCrawl()