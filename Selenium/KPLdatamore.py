import requests

cookies={   
    'pgv_pvid':'2702609282',
	'tvfe_boss_uuid':'b8981f6043448ac3',
	'pgv_pvi':'9469782016',
	'eas_sid':'S1w5Z424z5J8s6K4C7n3i8V6N0',
	'RK':'oKrp9MQgE3',
	'ptcz':'64e6a831c89f076553579a23dba0463e5ae4c73461c867c26c866c9872253257',
	'sd_userid':'49561545793586363',
	'sd_cookie_crttime':'1545793586363',
	'o_cookie':'763532119',
	'pac_uid':'1_763532119',
	'mobileUV':'1_1684b0f2598_d2ed9',
	'LW_uid':'J1i57520G4v7X3f4P5t8F1K4y8',
	'_ga':'GA1.2.677490607.1553506989',
	'ied_qq':'o0763532119',
	'LW_sid':'D1k5G6O0D3K1B3z3u8P9N0V2N5',
	'ts_uid':'8329707515',
	'ts_refer':'xui.ptlogin2.qq.com/cgi-bin/xlogin%3Fproxy_url%3Dhttps%3A//game.qq.com/comm-htdocs/milo/proxy.html%26appid%3D21000501%26target%3Dtop%26s_url%3Dhtt',
	'pgg_uid':'371561022',
	'pgg_appid':'101503919',
	'pgg_openid':'FDDDBFE5595512AF4C196C7BE1423580',
	'pgg_access_token':'074A29A1F2F2580CE373B0391C631858',
	'pgg_type':'1',
	'pgg_user_type':'5',
	'ptui_loginuin':'763532119',
	'pgv_info':'ssid=s6174772498',
	'ts_last':'datamore.qq.com/project/wzmatch/dist/index.html',
	'_qpsvr_localtk':'0.7908673727219715',
	'ptisp':'ctc',
	'pgv_si':'s142167040',
	'wxcode':'001Y84Mh10UG0v0X35Mh1jGZLh1Y84M5',
	'openid':'owanlssBw4zHhRSbD0SmBJOraNtE',
	'access_token':'22_nbr-jd8FGEG_J1bgj3hpKbujTc-YrjPKLstbJfzaLr6JQpADyiQph2-sEBfTL9z7Ju7DF-2cNIJLB8tmmVxK4eQS_69m080TwRwF_OUEPsk',
	'acctype':'wx',
	'appid':'wx95a3a4d7c627e07d',
	'dmwxsession':'22_nbr-jd8FGEG_J1bgj3hpKbujTc-YrjPKLstbJfzaLr6JQpADyiQph2-sEBfTL9z7Ju7DF-2cNIJLB8tmmVxK4eQS_69m080TwRwF_OUEPsk',
	'IED_LOG_INFO2':'userUin%3DowanlssBw4zHhRSbD0SmBJOraNtE%26nickName%3D%26userLoginTime%3D1561516114',
}
# cookies = 'pgv_pvid=2702609282; tvfe_boss_uuid=b8981f6043448ac3; pgv_pvi=9469782016; eas_sid=S1w5Z424z5J8s6K4C7n3i8V6N0; RK=oKrp9MQgE3; ptcz=64e6a831c89f076553579a23dba0463e5ae4c73461c867c26c866c9872253257; sd_userid=49561545793586363; sd_cookie_crttime=1545793586363; o_cookie=763532119; pac_uid=1_763532119; mobileUV=1_1684b0f2598_d2ed9; LW_uid=J1i57520G4v7X3f4P5t8F1K4y8; _ga=GA1.2.677490607.1553506989; ied_qq=o0763532119; LW_sid=D1k5G6O0D3K1B3z3u8P9N0V2N5; ts_uid=8329707515; ts_refer=xui.ptlogin2.qq.com/cgi-bin/xlogin%3Fproxy_url%3Dhttps%3A//game.qq.com/comm-htdocs/milo/proxy.html%26appid%3D21000501%26target%3Dtop%26s_url%3Dhtt; pgg_uid=371561022; pgg_appid=101503919; pgg_openid=FDDDBFE5595512AF4C196C7BE1423580; pgg_access_token=074A29A1F2F2580CE373B0391C631858; pgg_type=1; pgg_user_type=5; ptui_loginuin=763532119; pgv_info=ssid=s6174772498; ts_last=datamore.qq.com/project/wzmatch/dist/index.html; _qpsvr_localtk=0.7908673727219715; ptisp=ctc; pgv_si=s142167040; wxcode=001Y84Mh10UG0v0X35Mh1jGZLh1Y84M5; openid=owanlssBw4zHhRSbD0SmBJOraNtE; access_token=22_nbr-jd8FGEG_J1bgj3hpKbujTc-YrjPKLstbJfzaLr6JQpADyiQph2-sEBfTL9z7Ju7DF-2cNIJLB8tmmVxK4eQS_69m080TwRwF_OUEPsk; acctype=wx; appid=wx95a3a4d7c627e07d; dmwxsession=22_nbr-jd8FGEG_J1bgj3hpKbujTc-YrjPKLstbJfzaLr6JQpADyiQph2-sEBfTL9z7Ju7DF-2cNIJLB8tmmVxK4eQS_69m080TwRwF_OUEPsk; IED_LOG_INFO2=userUin%3DowanlssBw4zHhRSbD0SmBJOraNtE%26nickName%3D%26userLoginTime%3D1561516114'



res=requests.get('https://cgi.datamore.qq.com/datamore/smobac/player/index?page=1&page_size=20&start_date=2019-03-28&end_date=2019-06-26&sort_field=played&sort_dir=desc&season_id=all&export=0&acctype=weixin&location=cn',cookies=cookies)
print(res.json())