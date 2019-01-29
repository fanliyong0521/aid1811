import re
# print(dir(re))

# re.I 忽略大小写
# s = 'Hello world'
# pattern = r'hello World'
# regex = re.compile(pattern,flags=re.I)
# re.A 使用ASCII 字符
# s = 'Hello 你好'
# pattern = r'\w+'
# regex = re.compile(pattern,flags=re.A) ['Hello']

# re.S 使用.匹配\n 字符
# s = '''hello world 
# nihao CHina
# '''
# pattern = r'.+'
# regex = re.compile(pattern,flags=re.S) 
#['hello world \nnihao CHina\n']

# re.M 匹配每行开头结尾
# s = '''hello world
# nihao CHina
# '''
# pattern = r'world$'
# regex = re.compile(pattern,flags=re.M) 

# re.X 可以给正则表达式每行加#注释
s = 'abcdef'
pattern = r'''(ab)# 第一行分组
\w+# 任意字符串
(?P<dog>ef)# dog组
'''
regex = re.compile(pattern,flags=re.X) 

l = regex.findall(s)
print(l)