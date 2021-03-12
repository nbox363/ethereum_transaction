import logging
import time

import requests

logging.basicConfig(level=logging.DEBUG)

url_get_last_block = 'https://api.etherscan.io/api?module=proxy&action=eth_blockNumber'
url_block_detail_info = 'https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={num}&boolean=true'

last_block_number = int(requests.get(url_get_last_block).json()['result'], 16)
first_block_number = last_block_number - 100

transactions_info = {}

time.sleep(5)


def get_transactions_info():
    for block_number in range(first_block_number, last_block_number):
        res = requests.get(url_block_detail_info.format(num=hex(block_number)))

        transactions = res.json()['result']['transactions']

        for transaction in transactions:
            try:
                from_ = int(transaction['from'], 16)
                to = int(transaction['to'], 16)
                val = abs(int(transaction['value'], 16))
            except TypeError:
                logging.debug(f"cannot process transaction {transaction}, in block number {hex(block_number)}")
                continue

            try:
                transactions_info[from_] -= val
                transactions_info[to] += val
            except KeyError:
                transactions_info[from_] = val
                transactions_info[to] = val

        time.sleep(5)


def find_max():
    max = (0, 0)
    for k, v in transactions_info.items():
        if v > max[1]:
            max = k, v

    logging.debug(f'the address, the balance of which has changed the most {hex(max[0])}, changed to {max[1]}')
    print(f'the address, the balance of which has changed the most {hex(max[0])}, changed to {max[1]}')


if __name__ == '__main__':
    get_transactions_info()
    find_max()
