import requests

ret = requests.get("https://github.com/", timeout=1)

ret.close()