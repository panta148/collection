import requests
r = requests.get('https://w3schools.com/python/demopage.htm')
print(r.text)
print(r.status_code)
