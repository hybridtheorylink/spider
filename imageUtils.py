from PIL import Image
import urllib
import os
import Constant
import socket
def downloadImage(url,imgname=None):
   try:
      print('download imgage : %s'%url)
      socket.setdefaulttimeout(Constant.DOWNLOAD_TIME_OUT)
      if(url.endswith('.gif')):return
      if(imgname is  None):
         index = url.rindex('/')
         imgname =  Constant.IMAGE_PATH +  url[index+1:len(url)]
      data = urllib.request.urlretrieve(url,imgname)
      img = Image.open(imgname)
      if(min(img.size)<200):
         os.remove(imgname)
   except Exception as e:
       print(e)