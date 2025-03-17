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

def process_address(address_queue,line_number):
    account = Account.from_key(address_queue)
    adress = account.address



    def sign_message(message):
        # 编码消息
        message_hash = encode_defunct(text=message)

        # 签名消息
        signed_message = account.sign_message(message_hash)

        return signed_message

    def verify_signature(message, signature):
        message_hash = encode_defunct(text=message)
        recovered_address = Account.recover_message(message_hash, signature=signature)
        return recovered_address


    random_number = random.uniform(2.5, 15.5)
    # time.sleep(random_number)
    rpc = "https://polygon-mainnet.infura.io/v3/c62c98c65b624ed0a09ccd72792f2791"
    chain_id = 137
    add=adress[2:]

    # initiate_payment_data = f'0x87da377d000000000000000000000000{token_contract[2:]}000000000000000000000000000000000000000000000000000000000{hex(verify_ids_int1)[2:]}000000000000000000000000{adress1[2:]}00000000000000000000000000000000000000000000000{hex(can_claim_points_wei)[2:]}0000000000000000000000000000000000000000000000000000022b1c8c1227a000000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000041{signature[2:]}00000000000000000000000000000000000000000000000000000000000000'
    initiate_payment_data = f'0x731133e9000000000000000000000000{add}000000000000000000000000000000000000000000000000000000000000008a000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000'

    checksum_to_address = '0xfd63401d3440a9267d1d2fc55da383a61180b5a6'

    # 使用 wallet_manager 发送交易
    value_in_wei = int(0)
    web3 = Web3(Web3.HTTPProvider(rpc))

    checksum_wallet_address = Web3.to_checksum_address(adress)
    checksum_wallet_address11 = Web3.to_checksum_address(checksum_to_address)

    bei_lv = 1  # 固定倍率
    # max_fee_per_gas = int(gas_price * bei_lv)
    nonce = web3.eth.get_transaction_count(checksum_wallet_address)
    gas_price = web3.eth.gas_price
    gas_limit = web3.eth.estimate_gas({
        'to': checksum_wallet_address11,
        'from': checksum_wallet_address,
        'data': initiate_payment_data
    })
    # 创建交易
    transaction = {
        'to': checksum_wallet_address11,
        # 'from': checksum_wallet_address,
        'value': 0,
        'data': initiate_payment_data,
        'gas': 210000,  # 使用自动获取的 gas limit
        'gasPrice': gas_price,  # 设置 gasPrice
        # 'maxFeePerGas': max_fee_per_gas,  # 设定 maxFeePerGas，可以根据需求调整
        # 'maxPriorityFeePerGas': gas_price,
        'chainId': chain_id,
        'nonce': nonce,  # 确保包含 nonce

    }

    # 发送交易
    signed_txn = web3.eth.account.sign_transaction(transaction, address_queue)

    # 发送已签名的交易
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

    print(f"交易哈希: {tx_hash.hex()}")
    print(address_queue)

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
    file_path = r"C:\Users\Administrator\Desktop\复习题 2\新建文件夹 (2)\taker.txt" # 替换为你的文件路径

    # 配对文件和变量，从第700行开始处理
    main1(file_path, start_line=1)

    print("所有文件处理完成")


if __name__ == "__main__":
    main()


