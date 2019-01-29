import re

# pattern = r'(\w+):(\d+)'
# s = '张:1994,李:1995'
# 直接re调用
# l = re.findall(pattern,s)
# l = re.search(pattern,s).group()

# compile 对象调用
# regex =re.compile(pattern)
# l = regex.findall(s,pos = 0,endpos =8)
# print(l) # [('张', '1994'), ('李', '1')]

# l = re.split('\s+',r'Hello     World   nihao  Kitty')
# print(l) # ['Hello', 'World', 'nihao', 'Kitty']

s = re.sub(r'\s+','##','Hello     World   nihao  Kitty',2)
print(s) # Hello##World##nihao  Kitty

s = re.subn(r'\s+','##','Hello     World   nihao  Kitty',2)
print(s) #元组:返回替换后的字符串和替换个数 ('Hello##World##nihao  Kitty', 2)


