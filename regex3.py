import re

pattern = r'(ab)cd(?P<dog>ef)'

regex = re.compile(pattern)
# 获取match对象
obj = regex.search('abcdefghijk',pos=0,endpos=8)
# 获取obj属性变量
print(obj.pos) # 目标字符串开始位置
print(obj.endpos) # 目标字符串结束位置
print(obj.re) # 正则表达式
print(obj.string) # 目标字符串
print(obj.lastgroup) # 最后一组的名称
print(obj.lastindex) # 最后一组的序列号
print('=================================')
# obj方法
print(obj.span()) # 得到匹配内容的起止位置
print(obj.start()) # 匹配内容开始位置
print(obj.end()) # 匹配内容结束位置
print(obj.group()) # 整体匹配内容abcdef
print(obj.group(2)) # 第二组内容 ef
print(obj.group('dog')) # dog组内容 ef
print(obj.groupdict()) # 获取捕获组字典
print(obj.groups()) # 获取所有子组对应匹配内容





