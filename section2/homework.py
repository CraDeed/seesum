import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL = "https://ssl.pstatic.net/tveta/libs/1254/1254988/ac9de8b9d68e30f28b86_20190926135722548.jpg"

savePath1 = "C:/Users/CraDeed/Desktop/ATOM/goodman/test1.jpg"
savePath = "C:/Users/CraDeed/Desktop/ATOM/goodman"

f = dw.urlopen(imgURL).read()

with open(savePath1, 'wb') as pa:
    pa.write(f)

     
