


import requests
import json
import sys
import threading
import queue
import time
from datetime import datetime, timedelta
import hmac
import hashlib
import base64

from fake_useragent import UserAgent
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
import time
import json
import secrets
import uuid
import logging
from ecdsa import SigningKey, SECP256k1
from bech32 import bech32_encode, convertbits
import random
import itertools
import requests
import json
import sys
import threading
import queue
import time
import json
import secrets
import base64
import string
import requests
import os
import base64
import secrets
def process_address(address_queue,line_number):
    account = Account.from_key(address_queue)
    adress = account.address
    ua = UserAgent()

    rpc = "https://testnet.dplabs-internal.com"
    chain_id = 688688

    # 使用示例：

    initiate_payment_data = f'0x84bb1e42000000000000000000000000{adress[2:]}0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000de0b6b3a764000000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000016000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

    checksum_to_address = '0x822483f6cf39b7dad66fec5f4feecbfd72172626'

    # 使用 wallet_manager 发送交易
    value_in_wei = int(0)
    web3 = Web3(Web3.HTTPProvider(rpc))

    checksum_wallet_address = Web3.to_checksum_address(adress)
    checksum_wallet_address11 = Web3.to_checksum_address(checksum_to_address)
    balance_wei = web3.eth.get_balance(adress)
    balance_eth = web3.from_wei(balance_wei, 'ether')

    if int(balance_eth) > 1:
        bei_lv = 1  # 固定倍率
        # max_fee_per_gas = int(gas_price * bei_lv)
        nonce = web3.eth.get_transaction_count(checksum_wallet_address)
        gas_price = web3.eth.gas_price
        # gas_limit = web3.eth.estimate_gas({
        #     'to': checksum_wallet_address11,
        #     'from': checksum_wallet_address,
        #     'data': initiate_payment_data
        # })
        # 创建交易
        transaction = {
            'to': checksum_wallet_address11,
            # 'from': checksum_wallet_address,
            'value': Web3.to_wei(1, 'ether'),  # ,
            'data': initiate_payment_data,
            'gas': 210000,  # 使用自动获取的 gas limit
            'gasPrice': gas_price,  # 设置 gasPrice
            # 'maxFeePerGas': max_fee_per_gas,  # 设定 maxFeePerGas，可以根据需求调整
            # 'maxPriorityFeePerGas': gas_price,
            'chainId': chain_id,
            'nonce': nonce,  # 确保包含 nonce

        }

        signed_txn = web3.eth.account.sign_transaction(transaction, address_queue)

        # 发送已签名的交易
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        print(f"交易哈希: {tx_hash.hex()}")

    # 获取随机的 User-Agent
    user_agent = ua.random



#
    # bei_lv = 1  # 固定倍率
    # # max_fee_per_gas = int(gas_price * bei_lv)
    # nonce = web3.eth.get_transaction_count(checksum_wallet_address)
    # gas_price = web3.eth.gas_price
    # gas_limit = web3.eth.estimate_gas({
    #     'to': checksum_wallet_address11,
    #     'from': checksum_wallet_address,
    #     'data': initiate_payment_data
    # })
    # # 创建交易
    # transaction = {
    #     'to': checksum_wallet_address11,
    #     # 'from': checksum_wallet_address,
    #     'value': 0,
    #     'data': initiate_payment_data,
    #     'gas': 210000,  # 使用自动获取的 gas limit
    #     'gasPrice': gas_price*2,  # 设置 gasPrice
    #     # 'maxFeePerGas': max_fee_per_gas,  # 设定 maxFeePerGas，可以根据需求调整
    #     # 'maxPriorityFeePerGas': gas_price,
    #     'chainId': chain_id,
    #     'nonce': nonce,  # 确保包含 nonce
    #
    # }
    #
    # signed_txn = web3.eth.account.sign_transaction(transaction, address_queue)
    #
    # # 发送已签名的交易
    # tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    #
    # print(f"交易哈希: {tx_hash.hex()}")






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
        for _ in range(2):
            thread = threading.Thread(target=worker, args=(address_queue,))
            thread.start()
            threads.append(thread)

        # 等待所有任务完成
        address_queue.join()

        # 停止工作线程
        for _ in range(2):
            address_queue.put(None)
        for thread in threads:
            thread.join()

        print(f"{keys_file_path} 此地址处理完成")
    except Exception as e:
        print(f"处理文件 {keys_file_path} 时出错: {e}")


def main():
    file_path = r"/Users/fly/PyCharmMiscProject/.venv/主要代码/临时文件/pharos打乱"
    main1(file_path, start_line=1)

    print("所有文件处理完成")


if __name__ == "__main__":
    main()

