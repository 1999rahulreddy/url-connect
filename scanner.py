import requests
import re, urllib
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self,  url, ignore_links):
        self.session = requests.Session()
        self.t_url = url
        self.t_links = []
        self.ignore = ignore_links
        
    def get_links(self, url):
        response = self.session.get(url)
        a = str(response.content)
        return re.findall('(?:href=")(.*?)"', a)

    def crawl(self, url=None):
        if url == None:
            url = self.t_url
        link = self.get_links(url)
        for i in link:
            i = urllib.parse.urljoin(url, i)

            if "#" in i:
                i = i.split("#")[0]
                
            if self.t_url in i and i not in self.t_links and i not in self.ignore:
                self.t_links.append(i)
                print(i)
                self.crawl(i)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content)
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        for i in form_list:
            action = i.get("action")
            post_url = urllib.parse.urljoin(url, action)
            method = i.get("method")
            inputs = i.findAll("input")
            data1 = {}
            for j in inputs:
                input_name = j.get("name")
                input_type = j.get("type")
                if input_type == "text":
                    input_value = value
                data1[input_name] = input_value
            if method == "post":
                return self.session.post(post_url, data = data1)
            return self.session.get(post_url, params=data1)

    def run_scanner(self):
        for link in self.t_links:
            forms = self.extract_form(link)
            for f in forms:
                print("[+] Testing form in " + link)
            if "=" in link:
                print("[+] Testing " + link)
        
