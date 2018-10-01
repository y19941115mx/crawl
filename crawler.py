import requests
from util import *
import time
import json
from models import Post
from datetime import datetime
import logging
import html

class WXCrawler(object):
	"""微信公众号爬虫"""
	def __init__(self, url, headers=None):
		super(WXCrawler, self).__init__()
		self.url = url
		self.headers = headers

	def crawl(self, offset=0):
		url = self.url.format(offset=offset)
		headers = str_to_dict(self.headers)
		response = requests.get(url, headers=headers, verify=False)
		result = response.json()
		if result.get("ret") == 0:
			msg_list = result.get("general_msg_list")
			print("抓取数据：offset=%s, data=%s" % (offset, msg_list))
			self.save(msg_list)
           # 递归调用
			has_next = result.get("can_msg_continue")
			if has_next == 1:
				next_offset = result.get("next_offset")
				time.sleep(2)
				self.crawl(next_offset)
		else:
            # 错误消息
            # {"ret":-3,"errmsg":"no session","cookie_count":1}
			print("无法正确获取内容，请重新从Fiddler获取请求参数和请求头")
			exit()

	@staticmethod
	def save(msg_list):
		msg_list = msg_list.replace("\/", "/")
		data = json.loads(msg_list)
		msg_list = data.get("list")
		for msg in msg_list:
			p_date = msg.get("comm_msg_info").get("datetime")
			msg_info = msg.get("app_msg_ext_info")  # 非图文消息没有此字段
			if msg_info:
				WXCrawler._insert(msg_info, p_date)
				multi_msg_info = msg_info.get("multi_app_msg_item_list")
				for msg_item in multi_msg_info:
					WXCrawler._insert(msg_item, p_date)
			else:
				print(u"此消息不是图文推送，data=%s" % json.dumps(msg.get("comm_msg_info")))

	@staticmethod
	def _insert(item, p_date):
		keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
		sub_data = sub_dict(item, keys)
		post = Post(**sub_data)
		p_date = datetime.fromtimestamp(p_date)
		post["p_date"] = p_date
		print('save data %s ' % post.title)
		try:
			post.save()
		except Exception as e:
			print("保存失败 data=%s" % post.to_json(), exc_info=True)


	@staticmethod
	def update_post(data_url,data_headers,post):
		data_url_params = str_to_dict(data_url, "&", "=")
		 # url转义处理 文章链接
		content_url = html.unescape(post.content_url)
		content_url_params = str_to_dict(content_url, "&", "=")
        # 更新到data_url
		data_url_params.update(content_url_params)
        # form data
		body = "www.sdf.test?is_only_read=1&req_id=0414NBNjylwrVHDydtl3ufse&pass_ticket=zpU4AwNXTGS5LfBXFx4NCyMo5YTpSQo9RarrPG3tjhmMaGfORzykNNviX7IlM4i0&is_temp_url=0"
		data = str_to_dict(body, "&", "=")
        
		headers = str_to_dict(data_headers)
		data_url = "https://mp.weixin.qq.com/mp/getappmsgext"

		r = requests.post(data_url, data=data, verify=False, params=data_url_params, headers=headers)
		result = r.json()
		if result.get("appmsgstat"):
		            post['read_num'] = result.get("appmsgstat").get("read_num")
		            post['like_num'] = result.get("appmsgstat").get("like_num")
		            post['reward_num'] = result.get("reward_total_count")
		            post['u_date'] = datetime.now()
		            print("「%s」read_num: %s like_num: %s reward_num: %s" %
		                        (post.title, post['read_num'], post['like_num'], post['reward_num']))
		            post.save()
		else:
		    print(u"没有获取到真实数据，请检查请求参数是否正确，返回的数据为：data=%s" % r.text)
		    exit()




if __name__ == '__main__':
	# crawler = WXCrawler(url, headers)
	# crawler.crawl()
	results = Post.objects(read_num=0)
	print('剩余数据：%d' % (len(results),))

	for post in results:
		WXCrawler.update_post(data_url, data_headers, post)
		time.sleep(1)

    

