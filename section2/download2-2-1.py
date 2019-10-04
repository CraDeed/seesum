import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL = "http://cafefiles.naver.net/20151126_112/gunwoo0423_1448535959729YfC2I_JPEG/740_47d4878a3e974.jpeg"
htmlURL = "http://google.com"

savePath1 = "C:/Users/CraDeed/Desktop/ATOM/좋은사람/test1.jpg"
savePath2 = "C:/Users/CraDeed/Desktop/ATOM/좋은사람/index.html"

dw.urlretrieve(imgURL, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
