# Social Network
社交平台

## 微博
微博
### 个人信息
API : 'https://m.weibo.cn/api/container/getIndex?containerid=100505' + str(userid)
### 关注的人
API : 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_' + str(userid) + '&page=' + str(page)
***建议： 批量爬取个人信息时，使一个账号关注这些人，再爬取关注的人信息，单次请求可以获得10条个人信息***
### 个人微博
API : 'https://m.weibo.cn/api/container/getIndex?containerid=107603' + str(userid) + '&page=' + str(page)
### 单条微博
API : 'https://m.weibo.cn/statuses/show?id=' + str(id)
      'https://m.weibo.cn/api/statuses/show?id=' + str(id)
### 微博评论
API : 'https://m.weibo.cn/api/comments/show?id='+weiboId+'&page='+str(page)
### 热门微博
API : 'https://m.weibo.cn/api/container/getIndex?containerid=102803&page=' + str(page)
### 微博话题
API ：'https://m.weibo.cn/api/container/getIndex?containerid=231522type=61%26q=' + keyword + '%26page_type=searchall%26page=' + str(page)

## Tieba
百度贴吧
头条
玩加
NGA
虎扑
# Video Platform
快手
优酷
腾讯
爱奇艺
西瓜
微视
Bilibili
# Stream Platform
触手
斗鱼
战旗
虎牙
熊猫
火猫

