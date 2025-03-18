

import sys
import threading
import queue
import time
from fake_useragent import UserAgent
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
        proxies = {
            "http": "http://40074886-dat:yuxodmyl@47.76.43.121:1288",
            "https": "http://40074886-dat:yuxodmyl@47.76.43.121:1288"
        }
        def capsolver():
            api_key = ""  # your api key of capsolver
            site_key = "0x4AAAAAAA47SsoQAdSW6HIy"  # site key of your target site
            site_url = "https://app.testnet.initia.xyz/faucet"  # page url of your target site

            payload = {
                "clientKey": api_key,
                "task": {
                    "type": 'AntiTurnstileTaskProxyLess',
                    "websiteKey": site_key,
                    "websiteURL": site_url,
                    "metadata": {
                        "action": ""  # optional
                    }
                }
            }
            res = requests.post("https://api.capsolver.com/createTask", json=payload)
            resp = res.json()
            task_id = resp.get("taskId")
            if not task_id:
                print("Failed to create task:", res.text)
                return
            print(f"Got taskId: {task_id} / Getting result...")

            while True:
                time.sleep(1)  # delay
                payload = {"clientKey": api_key, "taskId": task_id}
                res = requests.post("https://api.capsolver.com/getTaskResult", json=payload)
                resp = res.json()
                status = resp.get("status")
                if status == "ready":
                    return resp.get("solution", {}).get('token')
                if status == "failed" or resp.get("errorId"):
                    print("Solve failed! response:", res.text)
                    return
        #
        token = capsolver()
        print(token)
        proxies = {
            "http": "",
            "https": ""
        }

        url = "https://faucet-api.testnet.initia.xyz/claim"

        payload = json.dumps({
            "address": address_queue,
            "turnstile_response": token
        })
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-HK,zh;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.testnet.initia.xyz',
            'priority': 'u=1, i',
            'referer': 'https://app.testnet.initia.xyz/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }

        response = requests.request("POST", url, headers=headers, data=payload,proxies=proxies)

        print(response.text)
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
        for _ in range(3):
            thread = threading.Thread(target=worker, args=(address_queue,))
            thread.start()
            threads.append(thread)

        # 等待所有任务完成
        address_queue.join()

        # 停止工作线程
        for _ in range(3):
            address_queue.put(None)
        for thread in threads:
            thread.join()

        print(f"{keys_file_path} 此地址处理完成")
    except Exception as e:
        print(f"处理文件 {keys_file_path} 时出错: {e}")

def main():
 
    file_path = r'C:\Users\Administrator\Desktop\复习题 2\initia 地址.txt'  # 替换为你的文件路径

   


    # 配对文件和变量

    main1(file_path)

    print("所有文件处理完成")


if __name__ == "__main__":
    attempts = 0
    while attempts < 10:
        main()

