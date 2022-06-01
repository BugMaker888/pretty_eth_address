from eth_account import Account
from multiprocessing import Process

def check_address(address):
    address = address[2:]
    # 开头4个字符相同，如0x8888...
    if address[0] == address[1] == address[2] == address[3]:
        return "aaaa_"
    # 结尾4个字符相同，如0x...8888
    if address[-1] == address[-2] == address[-3] == address[-4]:
        return "_aaaa"
    return None

def run():
    while True:
        account = Account.create()
        address = str(account.address)
        address_type = check_address(address)
        if not address_type:
            continue
        print(address)
        private_key = str(account._key_obj)
        with open(f"{address_type}.txt", "a+") as f:
            f.write(f"{address} {private_key}\n")
            f.close

if __name__ == "__main__":
    # 使用4进程运行
    for i in range(4):
        process = Process(target=run)
        process.start()
