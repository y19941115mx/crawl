url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzI3NjA0ODE1OQ==&f=json&offset={offset}&count=10&is_ok=1&scene=124&uin=MzQ3NDg1MTY3Nw%3D%3D&key=3e6d69d68316f4721416d82f75d5f03d67b6d4cde3cc82b74b53c994330bf6a79efdd84f58322fd93f43b284ff65da14a01b98128677d5715c97a6e035b81f58fd572cb190c229ed31099545a2c11396&pass_ticket=91ptuCROCZ4C5zdUaTDYMc1vJQOIHVSIx5C49K53rg6JNNuOE82lh941u1u4huPj&wxtoken=&appmsg_token=976_ajScd9FD6ZVO5lS4-6u6SBs0r-cX6RV8aWnMCQ~~&x5=0&f=json'

# 从 Fiddler 获取最新的请求头参数
headers = """
Host: mp.weixin.qq.com
Accept-Encoding: br, gzip, deflate
Cookie: devicetype=iMacMacBookAir52OSXOSX10.13.5build(17F77); lang=zh_CN; pass_ticket=91ptuCROCZ4C5zdUaTDYMc1vJQOIHVSIx5C49K53rg6JNNuOE82lh941u1u4huPj; version=12031110; wap_sid2=CN2O+PgMElwzQkNITnVEaW90UHRBS3dMTHNIWS1fNUZFRUJ5bjlUQmZtLXY4ZkY1ZWVuNGhNZzIwVFFLWnRjR1RpbF80MFVvanU5Qkk2cnZFbi1tUTd1SXppd05ZTkFEQUFBfjDkrsPdBTgNQJVO; wxuin=3474851677
Connection: keep-alive
Accept: */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI3NjA0ODE1OQ==&scene=124&uin=MzQ3NDg1MTY3Nw%3D%3D&key=3e6d69d68316f4721416d82f75d5f03d67b6d4cde3cc82b74b53c994330bf6a79efdd84f58322fd93f43b284ff65da14a01b98128677d5715c97a6e035b81f58fd572cb190c229ed31099545a2c11396&devicetype=iMac+MacBookAir5%2C2+OSX+OSX+10.13.5+build(17F77)&version=12031110&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=91ptuCROCZ4C5zdUaTDYMc1vJQOIHVSIx5C49K53rg6JNNuOE82lh941u1u4huPj
Accept-Language: zh-cn
X-Requested-With: XMLHttpRequest

"""


data_url = 'https://mp.weixin.qq.com/mp/getappmsgext?f=json&mock=&uin=MzQ3NDg1MTY3Nw%253D%253D&key=b9e0608486d8e297facd738aaee5a179034621139f84ed2d02462edb5702fcfdb074c200f8bb889dc56618a17709260895fc3b881342477832aa75ff6b187146233f4591aaa2fa756566141cc90f727d&pass_ticket=ukQHWJ7lVsRjKvhVCFRFIf0kuuU4SSvl4C15JxNtf3MxQy%25252BtQfCSU%25252BGnOj0U4X6H&wxtoken=777&devicetype=iMac%26nbsp%3BMacBookAir5%2C2%26nbsp%3BOSX%26nbsp%3BOSX%26nbsp%3B10.13.5%26nbsp%3Bbuild(17F77)&clientversion=12031110&appmsg_token=976_dPgcvvGqczfCboTojOJ3FB6dXlVWJfY7Om7_5evQUlkXnHhR9tNIyWMVJctHfSchTuAFmqr3nxMA0Mo_&x5=0&f=json'
data_headers = """
Host: mp.weixin.qq.com
Accept: */*
X-Requested-With: XMLHttpRequest
Accept-Language: zh-cn
Accept-Encoding: br, gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://mp.weixin.qq.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat
Connection: keep-alive
Referer: https://mp.weixin.qq.com/s?__biz=MzI3NjA0ODE1OQ==&mid=2651829695&idx=1&sn=0cbcac3ee74d1453b0a23a1af59a3a75&chksm=f08065cfc7f7ecd9f0b789c6b537d696a1881e5eac5fbb23ecd29691e411d11f0c58258a3c76&scene=0&key=b9e0608486d8e297facd738aaee5a179034621139f84ed2d02462edb5702fcfdb074c200f8bb889dc56618a17709260895fc3b881342477832aa75ff6b187146233f4591aaa2fa756566141cc90f727d&ascene=0&uin=MzQ3NDg1MTY3Nw%3D%3D&devicetype=iMac+MacBookAir5%2C2+OSX+OSX+10.13.5+build(17F77)&version=12031110&nettype=WIFI&lang=zh_CN&fontScale=100&pass_ticket=ukQHWJ7lVsRjKvhVCFRFIf0kuuU4SSvl4C15JxNtf3MxQy%2BtQfCSU%2BGnOj0U4X6H
Content-Length: 752
Cookie: devicetype=iMacMacBookAir52OSXOSX10.13.5build(17F77); lang=zh_CN; pass_ticket=ukQHWJ7lVsRjKvhVCFRFIf0kuuU4SSvl4C15JxNtf3MxQy+tQfCSU+GnOj0U4X6H; rewardsn=; version=12031110; wap_sid2=CN2O+PgMElxUM180a0dRck91ZnlLSEd1UzVqeUlRMEdnYmRTU05VdzZCV2t4MXZHV1psTlBYWWIzZXFFZXFVaFNUZ3VMNWxNeHhlanh4b19SOV9yNG51T3VCNnpkOUFEQUFBfjCY3cXdBTgNQAE=; wxtokenkey=777; wxuin=3474851677
"""

import html


def sub_dict(d, keys):
	return {k: html.unescape(d[k]) for k in d if k in keys}



def str_to_dict(s, join_symbol="\n", split_symbol=":"):
	if join_symbol == '&':
		s = s.split('?', 1)[1]
	s_list = s.split(join_symbol)
	data = {}
	for item in s_list:
		item = item.strip()
		if item:
			k, v = item.split(split_symbol, 1)
			data[k] = v.strip()
	return data

if __name__ == '__main__':
	print(str_to_dict(url, '&', '='))

