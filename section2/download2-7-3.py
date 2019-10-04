from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/"
res = req.urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(res, 'html.parser')

new = soup.select("div.column.course_item.is-one-fifth-desktop.is-4-tablet.is-half-mobile")
for i, e in enumerate(new,1):
    print(i," ",e.select("div.course_title")[0].string)
