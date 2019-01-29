import sys
from re import *

def get_address(port):
    # 提取一段内容
    f = open('1.txt')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line 
            else:
                break
        # 已经到文件结尾
        if not data:
            return 'Not Found'
        # print(data,end='')
        # 匹配首单词,查看是否为目标段落
        try:
            PORT = match(r'\S+',data).group()
            # print(PORT)
        except Exception as e: 
            print(e)
            continue
        if PORT == port:
            # pattern = r"address is ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})"
            pattern = r"address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknow)"
            addr = search(pattern,data).group(1)
            f.close()
            return addr


if __name__=='__main__':
    port = sys.argv[1]
    addr = get_address(port)
    print(addr)
    