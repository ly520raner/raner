from django.shortcuts import render
from blog.models import BlogsPost
def raner(request):
    db_list=BlogsPost.objects.all()
    return render(request,'raner.html',{'db_list':db_list})
