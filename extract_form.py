import requests
from bs4 import BeautifulSoup
import urllib

t_url = "http://192.168.56.102/mutillidae/index.php?page=dns-lookup.php"
#t_url = "http://avegaz.com"

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

response = request(t_url)
parsed_html = BeautifulSoup((response.content))
form_list = parsed_html.findAll("form")
for i in form_list:
    action = i.get("action")
    post_url = urllib.parse.urljoin(t_url, action)
    method = i.get("method")
    inputs = i.findAll("input")
    data1 = {}
    for j in inputs:
        input_name = j.get("name")
        input_type = j.get("type")
        if input_type == "text":
            input_value = "test"
        data1[input_name] = input_value
    result = requests.post(post_url, data = data1)
    print(result.content.decode('utf-8'))
