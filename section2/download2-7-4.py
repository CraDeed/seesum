from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
res = req.urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(res, 'html.parser')

top10 = soup.select("div.realtime_part > ol.list_hotissue.issue_row > li > div > div[aria-hidden='true'] > span.txt_issue > a")

for i, e in enumerate(top10,1):
    print(i, " " ,e.string)
