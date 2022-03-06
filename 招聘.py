import gevent
from gevent import monkey;monkey.patch_all()

from gevent.queue import Queue
import requests
import time
from fake_useragent import UserAgent
import pymysql
import random
import re
from bs4 import BeautifulSoup
import openpyxl


class zhaoping():

    def unsbox(self, arg1):
        array2 = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13,
                  6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36]
        array1 = [x for x in range(len(array2))]
        for i in range(len(arg1)):
            str3 = arg1[i]
            for j in range(len(array2)):
                if array2[j] == i + 1:
                    array1[j] = str3
        str2 = "".join(array1)

        return str2

    def hexXor(self, arg3):
        arg2 = "3000176000856006061501533003690027800375"
        i = 0
        str1 = ''
        while (i < len(arg3) and i < len(arg2)):
            num1 = arg3[i:i+2]
            obj1 = int(num1,16)
            num2 = arg2[i:i + 2]
            obj2 = int(num2, 16)
            str4 = '{:02x}'.format(obj1 ^ obj2)

            if len(str4) == 1:
                str4 = '0' + str4
            str1 += str4
            i += 2

        return str1

    def pares(self, arg1):
        middle_data = self.unsbox(arg1)
        result = self.hexXor(middle_data)
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
        middle_time = (time.time() + (3600 * 1000))
        strtime = time.strftime(GMT_FORMAT, time.gmtime(middle_time))
        cookies = result+ ";expires=" + strtime + ";max-age=3600;path=/"
        return cookies

    def random_ip(self):
        self.ip_list = []
        conn = pymysql.connect(
            host="xxxxxxx", user="root", passwd="xxxxxx", db="choose_position")
        cursor = conn.cursor()
        cursor.execute("select * from ip_address")
        result = cursor.fetchall()
        for row in result:
            self.ip_list.append(row[0])
        cursor.close()
        conn.close()


    def ask_data(self,i,j,count):
        proxies = {"http": random.choice(self.ip_list)}
        url_v = round(random.random(), 8)
        param = {
            'pageCode': '6019',
            'S_SOU_FULL_INDEX': 'PYTHON',
            'S_SOU_WORK_CITY': str(count+j),
            'pageIndex': str(i),
            'isEndPage': 'false',
            'at': '95a250c67b8f44f5bd0c9ba8cca508cf',
            'rt': 'ce8fc97bd1484c039cc652d58642a9e0',
            'channel': '',
            'utmsource': '',
            'platform': '7',
            '_v': url_v
        }      
        headers = {
            'cookie': 'urlfrom2=121113803; adfbid2=0; x-zp-client-id=1ffc2db5-eddf-4a1d-adb8-9935da1696ce; sts_deviceid=17cbb68262d1e5-0e27f847e3d0ad-561a145a-1049088-17cbb68262e2e3; x-zp-device-id=286d483ea0ad655d8cd22616b3f9f672; ZP_OLD_FLAG=false; locationInfo_search={%22code%22:%22689%22%2C%22name%22:%22%E9%BE%99%E5%B2%A9%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; selectCity_search=763; sts_sg=1; sts_chnlsid=121113803; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221117814551%22%2C%22first_id%22%3A%2217cbb6827cb17-0da47c74067622-561a145a-1049088-17cbb6827cc508%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22%24device_id%22%3A%2217cbb6827cb17-0da47c74067622-561a145a-1049088-17cbb6827cc508%22%7D; select_city_code=689; select_city_name=%E9%BE%99%E5%B2%A9; select_province_code=542; select_province_name=%E7%A6%8F%E5%BB%BA; sts_sid=17cc50ab688264-061cd0b5f955d5-731d2f20-46816-17cc50ab68b10; at=95a250c67b8f44f5bd0c9ba8cca508cf; rt=ce8fc97bd1484c039cc652d58642a9e0; sts_evtseq=2; zp_src_url=https%3A%2F%2Flanding.zhaopin.com%2F; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1635232910,1635393423; LastCity=%E9%BE%99%E5%B2%A9; LastCity%5Fid=689; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1635393444; acw_tc=ac11000116353934578222419e00d0c62eeebe5f60e7a65aee52f082def992; Hm_lvt_08e585d395455886ebe17d4b393b6523=1635250796,1635391546,1635393063,1635393462; Hm_lpvt_08e585d395455886ebe17d4b393b6523=1635393462',
            'user-agent': self.ua.random
        }
        request_list=[proxies,param,headers]
        return request_list


    def acquire_url(self,count):
        i=1
        a=True
        for j in range(12):
            while(a):
                requests_list=self.ask_data(i,j,count)
                res = requests.get(url="https://m.zhaopin.com/api/sou/search-position",
                           params=requests_list[1], proxies=requests_list[0], headers=requests_list[2])
                result = res.json()
                middle_list = result['data']['list']               
                if middle_list!= []:
                    for middle in middle_list:
                        if middle["positionURL"]:
                            self.work.put_nowait(middle["positionURL"])
                            print(middle["positionURL"])

                    i+=1
                else:
                    a=0
                time.sleep(1)
            else:
                a=True
                i=1
               

    def handle_url(self):
        while not self.work.empty():
            time.sleep(4.5)
            pattern = re.compile(r'var arg1 ?= ?[\'"](.*?)[\'"]')
            url = self.work.get_nowait()
            headers = {'user-agent': self.ua.random}
            with requests.session() as session:
                middle_info = session.get(url)
                arg1=pattern.findall(middle_info.text)
                if arg1:
                    cookies = {'acw_sc__v2': self.pares(arg1[0])}
                    with session.get(url, cookies=cookies) as res:
                        self.handle_data(res)

                else:
                    self.handle_data(middle_info)
                

    def handle_data(self,response):
        soup=BeautifulSoup(response.text,'html.parser')
        i=0
        try:
            position_name = soup.find('h3', class_="summary-plane__title").text     
            company_name = soup.find('a', class_="company__title").text
            print(position_name)
            company_address = soup.find('span', class_="job-address__content-text").text
       
            position_require = soup.find('div', class_="describtion__detail-content").text
     
            self.sheet.append([position_name, company_name, company_address, position_require])
        except AttributeError:
            print(1)
            
             
          
    

    def acquire_data(self):
        for j in range(2):
            self.acquire_url(540+j*12)
            task_list = []
            for  i in range(2):
                task=gevent.spawn(self.handle_url)
                task_list.append(task)
            gevent.joinall(task_list)
            self.wb.save("C:/Users/meteor/Desktop/代码/智联.xls")

    def __init__(self):
        self.random_ip()
        self.work=Queue()
        self.ua = UserAgent()
        self.wb=openpyxl.Workbook()
        self.sheet=self.wb.active
        self.sheet.title="智联"
        self.sheet.append(["职位名称","公司名称","公司地址","职位详情"])

x = zhaoping()
x.acquire_data()

