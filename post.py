import requests

t_url = "http://192.168.56.102/dvwa/login.php"
data = {"username":"admin", "password":"password", "Login":"submit"}
response = requests.post(t_url, data=data)
print(response.content.decode('utf-8'))
