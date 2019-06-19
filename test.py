import requests

res=requests.get('https://cgi.datamore.qq.com/datamore/smobac/player/index?page=1&page_size=20&start_date=2019-03-14&end_date=2019-06-12&sort_field=played&sort_dir=desc&season_id=all&export=0&acctype=qq&location=cn')
print(res.content)