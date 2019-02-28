import requests
import time,datetime,json,logging
import urllib.request
import urllib.parse


class HupuByUser():
    @staticmethod
    def getTopicInfo():
        pass

class NGAByUser():
    @staticmethod
    def getTopicInfo():
        pass

class TiebaByUser():
    @staticmethod
    def getTopicInfo():
        pass
    
class WanjiaByUser():
    @staticmethod
    def getTopicInfo():
        pass

class ToutiaoByUser():
    @staticmethod
    def getTopicInfo():
        pass
    
    @staticmethod
    def getUserInfo():
        pass

class baiduByIndex():
    @staticmethod
    def getIndex(keywords, date=datetime.datetime.now(), proxy=None):
        errmsg = keywords + '关键词' + date.strftime("%Y-%m-%d") + '指数抓取出错'
        data = []
        header = {
            'Cookie': 'BAIDUID=F1F1786490B0E4A99D6F6073859F409E:FG=1; PSTM=1537851849; BIDUPSID=83AE2881BE598A571EFA9DAD323ED833; __cfduid=df0f47f19a354fced19b2a40c8ac168651541654682; BDUSS=wyZy0wNXdTVHYxNDRnMFlNWEZjakhiZH5tUFBKdDU4SmtQTUo0b1RQM0RxRGxjQVFBQUFBJCQAAAAAAAAAAAEAAAB8tw4Y0e6zvzk2MjEyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMMbElzDGxJcWG; MCITY=-289%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; delPer=0; PSINO=5; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1550747261,1550747599,1550803665,1550804958; ZD_ENTRY=baidu; BDRCVFR[6OBCGFDnCzm]=mk3SLVN4HKm; H_PS_PSSID=; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1550824714; bdindexid=6deffejprpp95c24bnenthg443',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }  # 模拟浏览器访问url
        # keywords = 'kpl'
        for i in range(1, 8):
            try:
                # date = '2019-02-20'
                searchDate = date + datetime.timedelta(days=i - 8)
                errmsg = keywords + '关键词' + searchDate.strftime("%Y-%m-%d") + '指数抓取出错'
                url = 'https://index.baidu.com/api/SearchApi/index?area=0&word=' + keywords + '&startDate=' + searchDate.strftime(
                    "%Y-%m-%d") + '&endDate=' + searchDate.strftime("%Y-%m-%d")
                request = urllib.request.Request(url, headers=header)
                response = urllib.request.urlopen(request).read()
                resJson = json.loads(response)
                if resJson['data']['generalRatio'][0]['all']['yoy'] == '-':
                    continue
                kw_index_all = resJson['data']['generalRatio'][0]['all']['avg']
                kw_index_pc = resJson['data']['generalRatio'][0]['pc']['avg']
                create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data.append({'keywords': keywords, 'kw_index': resJson, 'kw_index_all': kw_index_all,
                             'kw_index_pc': kw_index_pc, 'kw_date': searchDate.strftime("%Y-%m-%d"),
                             'create_time': create_time})
            except Exception as e:
                logging.exception(e)
                print(errmsg)
        return data