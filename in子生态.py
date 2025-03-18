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
import secrets
import base64
import string
import requests
from datetime import datetime, timedelta
import random
import string
import logging


import base64
import itertools
import logging
def process_address(address_queue,line_number):

    try:

        ua = UserAgent()

        # 获取随机的 User-Agent
        user_agent = ua.random


        address = address_queue

        url = "https://api.infinityg.ai/api/v1/user/auth/wallet_login"

        payload = json.dumps({
            "loginChannel": "MAIN_PAGE",
            "walletChain": "Ethereum",
            "walletType": "metamask",
            "walletAddress":address,
            # "inviteCode": "9KYA58"
        })
        headers = {
            'accept': '*/*',
            'accept-language': 'zh-HK,zh;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.infinityg.ai',
            'priority': 'u=1, i',
            'referer': 'https://www.infinityg.ai/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user_agent
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data = response.json()
        token = data['data']["token"]
        def task(id):

            url = "https://api.infinityg.ai/api/v1/task/complete"

            payload = json.dumps({
                "taskId": id
            })
            headers = {
                'accept': '*/*',
                'accept-language': 'zh-HK,zh;q=0.9',
                'authorization': f'Bearer {token}',
                'content-length': '0',
                'content-type': 'application/json',
                'origin': 'https://www.infinityg.ai',
                'priority': 'u=1, i',
                'referer': 'https://www.infinityg.ai/',
                'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user_agent
            }


            response = requests.request("POST", url, headers=headers, data=payload)


            url1 = "https://api.infinityg.ai/api/v1/task/claim"
            response1 = requests.request("POST", url1, headers=headers, data=payload)

            print(response1.text)
            random_number = random.uniform(2.5, 7.5)
            time.sleep(random_number)
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        def list():

            url = "https://api.infinityg.ai/api/v1/task/list"

            payload = {}
            headers = {
                'accept': '*/*',
                'accept-language': 'zh-HK,zh;q=0.9',
                'content-length': '0',
                'content-type': 'application/json',
                'authorization': f'Bearer {token}',
                'origin': 'https://www.infinityg.ai',
                'priority': 'u=1, i',
                'referer': 'https://www.infinityg.ai/',
                'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)


        def checkin ():
            # random_number = random.uniform(13.5, 29.5)
            # time.sleep(random_number)

            url = "https://api.infinityg.ai/api/v1/task/checkIn/"

            payload = {}
            headers = {
                'accept': '*/*',
                'accept-language': 'zh-HK,zh;q=0.9',
                'authorization': f'Bearer {token}',
                'content-length': '0',
                'content-type': 'application/json',
                'origin': 'https://www.infinityg.ai',
                'priority': 'u=1, i',
                'referer': 'https://www.infinityg.ai/',
                'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user_agent
            }


            response = requests.request("POST", url, headers=headers, data=payload)


            data=response.json()
            print(data)
            code=data['code']
            if code==90000:
                print('签到成功')
                return True
        def complet(id):


            url = "https://api.infinityg.ai/api/v1/task/complete"
            url1 = "https://api.infinityg.ai/api/v1/task/claim"

            payload = json.dumps({
                "taskId": id
            })
            headers = {
                'accept': '*/*',
                'accept-language': 'zh-HK,zh;q=0.9',
                'authorization': f'Bearer {token}',

                'content-type': 'application/json',
                'origin': 'https://www.infinityg.ai',
                'priority': 'u=1, i',
                'referer': 'https://www.infinityg.ai/',
                'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            response1 = requests.request("POST", url1, headers=headers, data=payload)


            print(response1.text)

        # task(id='8')
        # task(id='9')
        # task(id='15')
        # task(id='7')
        attempts1 = 1
        max_attempts = 4
        attempts2 = 1
        attempts3 = 1
        attempts4 = 1



        result = checkin()


        # while attempts1 < max_attempts:
        #     result = checkin()
        #
        #     if result:  # 随机决定成功或失败
        #
        #         break
        #     else:
        #         print(address_queue,"签到失败，重试第", attempts1, "次")
        #         attempts1+=1







    except Exception as e:
       print(e)


def shuffle_lines_in_txt(file_path, output_file=None):
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # 读取所有行

        # 打乱行的顺序
        random.shuffle(lines)

        # 将打乱后的内容写回到文件或另存为新文件
        output_path = output_file if output_file else file_path
        with open(output_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)  # 写入打乱后的行

        print(f"行顺序已打乱并保存到文件: {output_path}")

    except FileNotFoundError:
        print(f"文件 {file_path} 未找到")


def worker(address_queue):
    while True:
        item = address_queue.get()
        if item is None:
            break
        address, line_number = item  # 解包 address 和 line_number
        try:
            process_address(address, line_number)  # 假设 process_address 是你定义的函数
        except Exception as e:
            print(f"处理地址 {address}（行号: {line_number}）时出错: {e}")
        finally:
            address_queue.task_done()  # 标记任务完成


def main1(path, start_line=1):
    try:
        keys_file_path = path
        address_queue = queue.Queue()

        # 读取文件并从指定行号开始处理
        with open(keys_file_path, 'r') as file:
            # 跳过前 start_line-1 行
            for line_number, address in enumerate(itertools.islice(file, start_line - 1, None), start=start_line):
                address = address.strip()
                address_queue.put((address, line_number))  # 将地址和行号一起放入队列

        # 创建和启动工作线程
        threads = []
        for _ in range(1):
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

        print(f"{keys_file_path} 此地址处理完成")
    except Exception as e:
        print(f"处理文件 {keys_file_path} 时出错: {e}")

def main():
    # file=r"C:\Users\Administrator\Desktop\yihhe.txt"
    # 使用示例
    file_path = r'C:\Users\Administrator\Desktop\复习题 2\in子.txt'  # 替换为你的文件路径
    output_file = r'C:\Users\Administrator\Desktop\复习题 2\in子.txt'  # 可选，保存打乱后的内容到新文件
    shuffle_lines_in_txt(file_path, output_file)
    file = output_file


    # 配对文件和变量

    main1(file)

    print("所有文件处理完成")


if __name__ == "__main__":
    while True:
        main()
        time.sleep(86400)


