from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
import requests
import json
import sys
import threading
import queue
import time
from fake_useragent import UserAgent
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
import time
import json
from DrissionPage.common import Keys
from datetime import datetime, timedelta
import secrets
import base64
import string
import requests
from datetime import datetime, timedelta
import random
import string
import poplib
from email.parser import BytesParser
from email import parser
from email.header import decode_header
import re
import imaplib
import email
from email.header import decode_header
import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
import re


def process_address(address_queue,line_number):

    url = "http://127.0.0.1:54345"
    headers = {'Content-Type': 'application/json'}
    ua = UserAgent()

    # 获取随机的 User-Agent
    user_agent = ua.random
    def connect(ws_url):
        options = ChromiumOptions()

        # 添加所需的启动参数
        # options.set_argument('--headless')  # 无头模式
        # options.set_argument('--disable-gpu')  # 禁用 GPU，适用于无头模式
        # options.set_argument('--window-size=1920x1080')  # 设置窗口大小

        # 传入 WebSocket URL 进行远程调试
        try:
            page = ChromiumPage(addr_or_opts=ws_url).latest_tab
        except Exception as e:
                print(e)



        return page

    def openBrowser(browser_id):
        json_data = {"id": f'{browser_id}'}
        res = requests.post(f"{url}/browser/open", data=json.dumps(json_data), headers=headers).json()
        data = res['data']['ws']
        ws_url = data.split('/devtools')[0].replace('ws://', '')

        return ws_url
    def close(browser_id):
        json_data = {
            "id":browser_id


        }
        res = requests.post(f"{url}/browser/close", data=json.dumps(json_data), headers=headers)


    def id():
        json_data = {
            "page": 1,
            "pageSize": 100

        }

        res = requests.post(f"{url}/browser/list", data=json.dumps(json_data), headers=headers)

        res1 = res.json()

        all_ids = [item['id'] for item in res1['data']['list']]
        for id_value in all_ids:
            print(id_value)



    def PAILIE():
        url = "http://127.0.0.1:54345"
        headers = {'Content-Type': 'application/json'}
        res = requests.post(f"{url}/windowbounds/flexable", headers=headers).json()

    try:

        res = openBrowser(browser_id='d1dfacca686a4d6a8d82b25747c43f1b')

        page = connect(res)

        try:
            page.get('https://wump.xyz/')
            time.sleep(3)
            click3 = page.ele(
                f'xpath://*[@id="radix-:r4:-content-today"]/div[2]/div[1]/button')
            click3.click()
            time.sleep(3)
        finally:
            close(address_queue)


    except:
            print('1')








    #
    #







        # DC(url1='https://discord.gg/avituslabsxyz')






        # close(browser_id=address_queue)











def worker(address_queue):
    while True:
        address, line_number = address_queue.get()
        if address is None:
            break
        try:
            process_address(address, line_number)
        except Exception as e:
            print(f"处理地址 {address} 时出错: {e}")
        finally:
            address_queue.task_done()  # 标记任务完成

def main1(path):
    try:
        keys_file_path = path
        address_queue = queue.Queue()

        # 读取地址并加上行号
        with open(keys_file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                address = line.strip()
                address_queue.put((address, line_number))

        # 创建和启动10个工作线程
        threads = []
        for _ in range(1):  # 可根据需要调整线程数量
            thread = threading.Thread(target=worker, args=(address_queue,))
            thread.start()
            threads.append(thread)

        # 等待所有任务完成
        address_queue.join()

        # 停止工作线程
        for _ in range(1):
            address_queue.put(None)
        for thread in threads:
            thread.join()
        print(keys_file_path, "此地址处理完成")
    except Exception as e:
        print(f"处理文件 {keys_file_path} 时出错: {e}")

def main():
    file = r"C:\Users\Administrator\Desktop\skl id.txt"
    main1(file)

    print("所有文件处理完成")

if __name__ == "__main__":
    main()


