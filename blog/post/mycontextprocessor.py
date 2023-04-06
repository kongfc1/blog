#coding=utf-8
from django.db.models import Count

from post.models import Post


def getRightInfo(request):
    right_catepost = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('c')

    r_recpost = Post.objects.all().order_by('created')[:3]
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select date_format(created,'%Y/%m') created,count('*') c from t_post group by date_format(created,'%Y/%m')")
    arch = cursor.fetchall()
    return {'right_catepost':right_catepost,'r_recpost':r_recpost,'arch':arch}

















