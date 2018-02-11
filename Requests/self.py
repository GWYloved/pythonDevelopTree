import urllib2
import urllib
import datetime
import re
import os.path


big_path="/Users/yinpengcheng/Desktop/"

def save_file(this_download_url,path = big_path+"111.mp4"):
    print"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    time1=datetime.datetime.now()
    print str(time1)[:-7],
    if (os.path.isfile(path)):
        file_size=os.path.getsize(path)/1024/1024
        print "File "+path+" ("+ str(file_size)+"Mb) already exists."
        return
    else:
        print "Downloading "+path+"..."
        f = urllib2.urlopen(this_download_url)
        data = f.read()
        with open(path, "wb") as code:
            print "loading"
            code.write(data)
        time2=datetime.datetime.now()
        print str(time2)[:-7],
        print path+" Done."
        use_time=time2-time1
        print "Time used: "+str(use_time)[:-7]+", ",
        file_size=os.path.getsize(path)/1024/1024
        print "File size: "+str(file_size)+" MB, Speed: "+str(file_size/(use_time.total_seconds()))[:4]+"MB/s"

save_file("https://vid-egc.xvideos-cdn.com/videos/3gp/c/3/5/xvideos.com_c35cb91af4cac045177c4b57e9f7eb0c.mp4?_U1S5y3RF8HNI6xdOJnT6gHLNZ36H4Gs2J8xUOq2Rs748hx4nUUFHkK1-dOCME3JGy14nrkpVscJeBFvCa1bnCBqTi5HJ0TaEzIOcugrDbgO2TaZTTMFJEHpFpNSgXeSDp3OshaOqXJ56luqDra0Cbux51uECIPhIVbDSDuFlsdvrStPe50anLZm7_QWPEPu6vNj3NP7UWM")