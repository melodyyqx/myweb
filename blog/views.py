from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog.models import Blog
# Create your views here.


def blog(request):
    list_blog = Blog.objects.all()
    for blog in list_blog:
        print(blog.title)
        print(blog.time)
        print(blog.body)
    return render_to_response('blog.html', {"blogs":list_blog})


def login(request):
    return render(request,'login.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('user','')
        password = request.POST.get('pwd','')
        if username == "yqx" and password == "qaz12345":
             return HttpResponse("login success")
        else:
             return HttpResponse("login failed")
    else:
        return HttpResponse("not post!")