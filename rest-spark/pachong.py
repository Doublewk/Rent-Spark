import requests
import random
from bs4 import BeautifulSoup
import csv

file=open(r'D:\rent.csv','w',encoding="utf-8")

#伪装请求头
user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

def getHeaders():
    user_agent = user_agents[random.randint(0, len(user_agents)-1)] 
    headers = {
        'User-Agent': user_agent
    }
    return headers

def get_data(url):
    web_data = requests.get(url,headers=getHeaders(),stream=True).content.decode('utf8')
    soup = BeautifulSoup(web_data, 'html.parser')
    shuju=soup.findAll("div",class_="maincontent")[0].findAll('b')
    shuju1=soup.findAll("p",class_="details-item tag")
    shuju2=soup.findAll("address",class_='details-item')
    cengshu_list=[]
    lianxiren_list=[]
    weizhi_list=[]
    for i in shuju2:
        weizhi=i.get_text().split('\n')[1]+i.get_text().split('\n')[2].strip(' ')
        if ',' in weizhi:
            weizhi=weizhi.replace(","," ")
        weizhi_list.append(weizhi)
    for i in shuju1:
        cengshu=i.get_text().split('|')[2].split('\n')[0].split('\ue147')[0].strip(' ')
        cengshu_list.append(cengshu)
        lianxiren=i.get_text().split('|')[2].split('\n')[0].split('\ue147')[1].strip(' ')
        lianxiren_list.append(lianxiren)
    for i in range(((len(shuju))//5)):
        jianjie=shuju[i*5].get_text().replace("\n","")
        if ',' in jianjie:
            jianjie=jianjie.replace(","," ")
        fangxing=shuju[i*5+1].get_text()
        fangxing1=shuju[i*5+2].get_text()
        daxiao=shuju[i*5+3].get_text()
        jiage=shuju[i*5+4].get_text()
        rent=str(jianjie)+','+str(fangxing)+"室"+fangxing1+"厅"+','+str(daxiao)+"平米"+','+str(weizhi_list[i])+','+str(lianxiren_list[i])+','+str(jiage)+'\n'
        rent_list.append(rent)
    return rent_list

pages = ['https://zz.zu.anjuke.com/fangyuan/jinshui/fx2-p{}/'.format(x) for x in range(1,29)]

rent_list=[]
count = 0
for page in pages:
    rent=list(get_data(page))
    #反反爬虫策略2：每次爬取随机间隔3-10s
    #time.sleep(random.randint(3,10))
    count=count+1
    print ('the '+str(count)+' page is sucessful')

for i in rent:
    file.write(i)
file.close()
