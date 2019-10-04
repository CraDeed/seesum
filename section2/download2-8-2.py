from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# opener = req.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# req.install_opener(opener)

url = "https://www.inflearn.com/"

res = req.urlopen(url)
savePath = "C:/Users/CraDeed/Desktop/ATOM/goodman/section2/imgdown/"

try:
    if not os.path.isdir(savePath):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패")
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select("div.column.course_item.is-one-fifth-desktop.is-4-tablet.is-half-mobile > div > a")

for i, e in enumerate(img_list, 1):
    with open(savePath+"title_"+str(i)+".txt", 'wt') as f:
        f.write(e.select_one("div.course_title").string)

    fullFileName = os.path.join(savePath, savePath + str(i)+".jpg")
    quote = rep.quote_plus(e.select_one("figure.image.is_thumbnail > img")['src'][97:])
    req.urlretrieve(e.select_one("figure.image.is_thumbnail > img")['src'][:97] + quote, fullFileName)

print("다운로드 완료!")
