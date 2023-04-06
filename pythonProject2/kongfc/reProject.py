import re
# line = "qwertyuiop"
# s = "qwertyuiopl"
# print(re.match(line,s).group())
#
# line1 = 'Hello 123 456 World_This is Regex Demo'
# result = re.match('Hello\s\d\d\d\s\d{3}\s\w{10}',line1)
# print(result.group())
# str = 'rrr\frrr'
# str1 = r'rww\ds\gf'
# print(str)
# print(str1)
# re1 = re.match('^d[0-9]{2}hhh$','d12hhh')
# print(re1.group())
#
# res = re.match(r"<([a-zA-Z]*)>\w*</\1>","<html>hh</html>")
# print(res.group())

ret = re.search(r"\d+","于都理解999")
print(ret.group())
red = re.findall(r"\d+","python=999,c = 789")
print(red)
resub = re.sub(r"\d+",'999',"python=123")
print(resub)
resplit = re.split(r":| ","info:xiao 7")
print(resplit)
print(resplit[0])










