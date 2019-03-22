import requests

form = {"key":{"module":"pgg_dc_access_mt_svr","method":"keepalive","param":{"params":{"info":{"aid":"605976197","beat_report":"{\"str_pid\":\"605976197_1552964266\",\"scene_flag\":4096,\"source\":1,\"str_id\":\"503367680\",\"report_info\":{\"platform\":4,\"scenes\":4096,\"aid\":605976197,\"appid\":\"2000000133\",\"pid\":\"605976197_1552964266\",\"vid\":\"\",\"rid\":\"\",\"lid\":\"\",\"match_id\":\"\",\"tid\":\"\",\"nid\":\"\",\"category_id\":\"\",\"gift_id\":\"\",\"url\":\"\",\"room_id\":\"\",\"page_id\":\"2701\",\"login_type\":0,\"uin\":0,\"open_id\":0,\"pvid\":\"503367680\",\"terminal_type\":2,\"ch\":\"\",\"page_referer\":\"\",\"hbeat_ext\":{\"info\":{\"defunct\":\"0\"}}}}"}},"position":{"page_id":"QG_HEARTBEAT_PAGE_LIVE_ROOM"},"refer":{"seq":0,"tm":1553223718158,"context":"","seq_list":{"605976197":1553223721,"unhandle_events_num":0},"auto_incre_seq":128}}}}

url = 'https://share.egame.qq.com/cgi-bin/pgg_dc_async_fcgi?app_info={"platform":4,"terminal_type":2,"egame_id":"egame_official","imei":"","version_code":"9.9.9.9","version_name":"9.9.9.9"}&g_tk=&p_tk=&tt=1&_t: 1553223728409'
# url = 'https://egame.qq.com/605976197'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

res = requests.post(url,data=form,headers = header)
print(res.text)