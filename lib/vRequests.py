import requests
import settings
#settings.init()

class vRequests(object):
    
    def custom(self,url):
        proxies = headers = cookies = {}
		# Use custom user-agent
        if settings.settings["user-agent"] != "":
            headers.update({'user-agent': settings.settings["user-agent"]})
		# Use custom proxy
        if settings.settings["proxy"] == "on":
            proxies = self.set_proxies()
		# Use cookies
        if settings.settings["cookies"] != "":
            cookies = settings.settings["cookies"]
	
        r = requests.get(url,headers=headers,proxies=proxies,cookies=cookies)
        return r

    def set_proxies(self):
       http_proxy = https_proxy = settings.settings["http-proxy"]
       if settings.settings["https-proxy"] != "":
           https_proxy = https_proxy
       
       return {
          'http':  http_proxy,
          'https': https_proxy,
          } 
    