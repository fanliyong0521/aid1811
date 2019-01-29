import re

f = open('test.txt')
s = f.read()
pattern = r'[A-Z]+\w*' # 大写字母开头的单词
# 整数，小数，负数，分数，百分数
# 123 123.123% -123 1/123 123% 12.3%
pattern1 = r'-?0\.\d+%|-?\d+\.?\d+%|-?0\.\d+|-?\d+\.\d+|-?\d+/[1-9]+|-?[1-9]\d+'
pattern2 = r'-?\d+\.?/?\d*%?'

regex = re.findall(pattern,s)
regex1 = re.findall(pattern1,s)
regex2 = re.findall(pattern2,s)

print(regex)
print(regex1)
print(regex2)
f.close()

