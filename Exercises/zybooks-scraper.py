import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import urllib.request


def save_code():
    # param for token -> auth_token=

    auth_token = get_zybooks_auth_token()

    url = 'https://learn.zybooks.com/zybook/MSUCSE331OnsayFall2018/chapter/28/section/3?auth_token='+auth_token
    param = {'auth_token': auth_token}
    head = {"accept": 'text/html,application/xhtml+xml'}

    # page = requests.get(url, params=param, headers=head)
    #
    # with open('test.html', 'w', encoding='UTF-8') as file:
    #     file.write(str(page.text))

    #print(page.content)

    browser = webdriver.Chrome('/Users/tonysulfaro/Downloads/chromedriver')  # replace with .Firefox(), or with the browser of your choice
    #url = "http://example.com/login.php"
    browser.get(url)  # navigate to the page
    innerHTML = browser.execute_script("return document.body.innerHTML")
    with open('test.html', 'w', encoding='UTF-8') as file:
        file.write(innerHTML)


def get_zybooks_auth_token():
    email = 'sulfaroa@msu.edu'  # input('email:')
    password = 'Yes123456'  # input('password:')

    user_pass_dict = {'email': email, 'password': password}

    response = requests.post('https://zyserver.zybooks.com/v1/signin', json=user_pass_dict,
                             headers={"content-type": "application/json"})
    json_data = response.json()
    auth_token = json_data['session']['auth_token']
    print(auth_token)

    return auth_token


if __name__ == '__main__':
    save_code()
