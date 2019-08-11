import requests
url="http://m10.music.126.net/20190811101448/8c7aaedec3c52f9c0c16f6d6334cc342/ymusic/76b4/dcbb/0a65/9198b18815ee8ce42ae368ae29276f78.mp3"
path="绿色.mp3"
r=requests.get(url)
print ("ok")
with open(path,"wb") as f:
    f.write(r.content)
f.close()
