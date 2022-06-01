# ETH靓地址生成工具

1、先安装`eth_account`库，在终端执行命令：
``` bash
pip install eth_account
```

2、执行以下命令运行工具：
``` bash
python pretty_eth_address.py
```

3、可以根据电脑CPU核数，在代码里修改进程数：
``` python
if __name__ == "__main__":
    # 使用4进程运行
    for i in range(4):
        process = Process(target=run)
        process.start()
```
