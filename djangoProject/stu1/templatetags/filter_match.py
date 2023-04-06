#coding=utf-8
#自定义过滤器
from django.template import Library

register = Library()

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)

@register.filter
def splitstr(value,args):
    start,end = args.split(',')
    print(value.encode('utf-8'))
    value= value.encode('utf-8').decode('utf-8')
    print(start+'  '+end)
    return value[int(start):int(end)]