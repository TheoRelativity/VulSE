import requests
import settings
#settings.init()

class vRequests(object):
    
    def custom(self,url,parameters={}):
        proxies = headers = cookies = data = {}
		# Use custom user-agent
        if settings.settings["user-agent"] != "":
            headers.update({'user-agent': settings.settings["user-agent"]})
		# Use custom proxy
        if settings.settings["proxy"] == "on":
            proxies = self.set_proxies()
		# Use cookies
        if settings.settings["cookies"] != "":
            cookies = settings.settings["cookies"]
		# Set Post
        if "method" in parameters and parameters["method"] == "post":
            if "data" in parameters:
                data = parameters["data"]
                r = requests.post(url,headers=headers,proxies=proxies,cookies=cookies,data=data)
        else:
            r = requests.get(url,headers=headers,proxies=proxies,cookies=cookies,data=data)

        bad_request = True if (r.status_code == requests.codes.ok) else False
      
        result = {
             "bad_request": bad_request,
             "code": r.status_code,
             "text": r.text,
             "url":  r.url			 
                }
        return result

    def set_proxies(self):
       http_proxy = https_proxy = settings.settings["http-proxy"]
       if settings.settings["https-proxy"] != "":
           https_proxy = https_proxy
       
       return {
          'http':  http_proxy,
          'https': https_proxy,
          } 
    