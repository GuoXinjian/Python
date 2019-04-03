from urllib import request
import requests
import json
import time
import math
import hashlib
import re
from bs4 import BeautifulSoup
import email
import smtplib
from email.header import Header                  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText             # 发送正文只包含简单文本的邮件，引入MIMEText即可


# 发件人和收件人
sender = 'yangchen@vspn.cn'
receiver = '798176504@qq.com'

# 所使用的用来发送邮件的SMTP服务器
smtpServer = 'smtp.163.com'

# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username = 'XXXXXXXXXXX'
password = 'XXXXXXXX'

mail_title = '这里是邮件的主题'
mail_body = '这里是邮件的正文'

# 创建一个实例
message = email.mime.MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
message['From'] = sender  # 邮件上显示的发件人
message['To'] = receiver  # 邮件上显示的收件人
message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

try:
    smtp = smtplib.SMTP()  # 创建一个连接
    smtp.connect(smtpServer)  # 连接发送邮件的服务器
    smtp.login(username, password)  # 登录服务器
    smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
    print("邮件发送成功！！！")
    smtp.quit()
except smtplib.SMTPException:
    print("邮件发送失败！！！")





# 数值处理
# def toInt(str):
#     # str = str.replace('播放', '')
#     # str = str.replace('赞', '')
#     # str = str.replace('评论', '')
#     # str = str.replace('阅读', '')
#     if 'w' in str or '万' in str:
#         num = float(re.findall(r"\d+\.?\d*", str)[0])
#         num = num * 10000
#     else:
#         num = float(re.findall(r"\d+\.?\d*", str)[0])
#     return num
#
# str = '900宝'
# print(toInt(str))
# def get_url(max_behot_time, AS, CP):
#     url = 'https://www.toutiao.com/api/pc/feed/?category=news_society&utm_source=toutiao&widen=1' \
#           '&max_behot_time={0}' \
#           '&max_behot_time_tmp={0}' \
#           '&tadrequire=true' \
#           '&as={1}' \
#           '&cp={2}'.format(max_behot_time, AS, CP)
#     return url
#
#
# def get_ASCP():
#     t = int(math.floor(time.time()))
#     e = hex(t).upper()[2:]
#     m = hashlib.md5()
#     m.update(str(t).encode(encoding='utf-8'))
#     i = m.hexdigest().upper()
#
#     if len(e) != 8:
#         AS = '479BB4B7254C150'
#         CP = '7E0AC8874BB0985'
#         return AS, CP
#     n = i[0:5]
#     a = i[-5:]
#     s = ''
#     r = ''
#     for o in range(5):
#         s += n[o] + e[o]
#         r += e[o + 3] + a[o]
#
#     AS = 'AL' + s + e[-3:]
#     CP = e[0:3] + r + 'E1'
#     # print("AS:"+ AS,"CP:" + CP)
#     return AS, CP
#
#
# def download(title, news_url):
#     # print('正在爬')
#     req = request.urlopen(news_url)
#     if req.getcode() != 200:
#         return 0
#
#     res = req.read().decode('utf-8')
#     # print(res)
#     pat1 = r'content:(.*?),'
#     pat2 = re.compile('[\u4e00-\u9fa5]+')
#     result1 = re.findall(pat1, res)
#     # print(len(result1))
#     if len(result1) == 0:
#         return 0
#     print(result1)
#     result2 = re.findall(pat2, str(result1))
#     result3 = []
#     for i in result2:
#         if i not in result3:
#             result3.append(i)
#     # print(result2)
#     title = title.replace(':', '')
#     title = title.replace('"', '')
#     title = title.replace('|', '')
#     title = title.replace('/', '')
#     title = title.replace('\\', '')
#     title = title.replace('*', '')
#     title = title.replace('<', '')
#     title = title.replace('>', '')
#     title = title.replace('?', '')
#     with open(r'D:\code\python\spider_news\Toutiao_news\society\\' + title + '.txt', 'w') as file_object:
#         file_object.write('\t\t\t\t')
#         file_object.write(title)
#         file_object.write('\n')
#         file_object.write('该新闻地址：')
#         file_object.write(news_url)
#         file_object.write('\n')
#         for i in result3:
#             # print(i)
#             file_object.write(i)
#             file_object.write('\n')
#     # file_object.write(tag.get_text())
#     # print('正在爬取')
#
#
# def get_item(url):
#     # time.sleep(5)
#     cookies = {'tt_webid': '6478612551432734221'}
#     wbdata = requests.get(url, cookies=cookies)
#     wbdata2 = json.loads(wbdata.text)
#     data = wbdata2['data']
#     for news in data:
#         title = news['title']
#         news_url = news['source_url']
#         news_url = 'https://www.toutiao.com' + news_url
#         print(title, news_url)
#         if 'ad_label' in news:
#             print(news['ad_label'])
#             continue
#         download(title, news_url)
#     next_data = wbdata2['next']
#     next_max_behot_time = next_data['max_behot_time']
#     # print("next_max_behot_time:{0}".format(next_max_behot_time))
#     return next_max_behot_time
#
#
# if __name__ == '__main__':
#
#     refresh = 50
#     for x in range(0, refresh + 1):
#
#         print('第{0}次：'.format(x))
#         if x == 0:
#             max_behot_time = 0
#         else:
#             max_behot_time = next_max_behot_time
#             # print(next_max_behot_time)
#         AS, CP = get_ASCP()
#         url = get_url(max_behot_time, AS, CP)
#         next_max_behot_time = get_item(url)