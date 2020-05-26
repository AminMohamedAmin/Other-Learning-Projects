#لازم يكون الموقع اللي هتشتغل عليه معموله رن
from bs4 import BeautifulSoup
import urllib.request

file = open('web.txt', 'w')
site = urllib.request.urlopen('http://127.0.0.1:8000/').read()
soup = BeautifulSoup(site,'lxml')

file.write(str(soup.prettify()) + '\n') #فانكشن لتنسيق الكلام

# file.write(str(soup.title.string) + '\n') # يطبع اسم الصفحة
#
# file.write(str(soup.title.text) + '\n') #== string
#
# file.write(str(soup.p) + '\n') #يطبع اول تاج p تقابله
#
# for i in soup.find_all('p'):
#     file.write(str(i) + '\n')
#
# for i in soup.find_all('p'):
#     file.write(str(i.string) + '\n')

######### display specific part from page #########
# nav = soup.nav
# file.write(str(nav) + '\n')
# file.write(str(nav.text) + '\n') # بيجيب كل النصوص اللي بين التاجاات داخل الناف
# file.write(str(nav.string) + '\n') #بيجيب النصوص اللى تحت الناف فقط و اما اللي دتخا تاجات اخري مبيجبهاش
# for url in nav.find_all('a'):
#     file.write(str(url) + '\n')
#     file.write(str(url.get('href')) + '\n')
###################################################
###################################################
###################################################
####### get data from table ############
# from bs4 import BeautifulSoup
# import urllib.request
#
# file = open('web.txt', 'w')
# site = urllib.request.urlopen('http://127.0.0.1:8000/templates/data.html').read()
# soup = BeautifulSoup(site,'lxml')
#
# table = soup.table
# tr = table.find_all('tr')
# for row in tr:
#     td = row.find_all('td')
#     rows = [i.text for i in td]
#     file.write(str(rows) + '\n')
################################################33
#################################################
# يوجد طريقة اخري باستخدام مكتبة اخري
# import pandas as pd
#
# file = open('web.txt', 'w')
# table = pd.read_html('http://127.0.0.1:8000/templates/data.html', header=0)
# for td in table:
#     file.write(str(td) + '\n')