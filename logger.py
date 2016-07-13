import Constant
def log(str):

    fo = None
    try:
        #记录抓取网页的日志,不存在则创建文件
        fo = open(Constant.LOG_FILE, 'r+')
    except Exception as e:
        fo = open(Constant.LOG_FILE, 'w')
        print(e)
    try:
        fo.seek(0, 2)
        fo.write(str+'\n')
    except Exception as e:
        print(e)
    finally:
        fo.close()
