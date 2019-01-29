import re

# pattern = r'\d+'
s = '2018年中国经济增长6.6%,与2017年基本持平,2019面临很多困难'
# it = re.finditer(pattern,s)
# match匹配对象属性
# print(dir(next(it)))
# for i in it:
#     print(i.group()) # 通过匹配对象group属性,来获取匹配内容
# try:    
#     obj = re.fullmatch(r'\w+','hello1973')
#     print(obj.group())
# except AttributeError as e:
#     print(e)

# try:    
#     obj = re.match(r'[A-Z]\w+','xx Hello world')
#     print(obj.group())
# except AttributeError as e:
#     print(e)


try:    
    obj = re.search(r'\d+',s)
    print(obj.group()) # 只匹配第一处内容
except AttributeError as e:
    print(e)