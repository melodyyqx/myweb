from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.

@login_required()
def blog(request):
    list_blog = Blog.objects.all()
    for blog in list_blog:
        print(blog.title)
        print(blog.time)
        print(blog.body)
    #username = request.COOKIES.get('username','')
    username = request.session.get('username','')
    return render_to_response('blog.html', {"blogs":list_blog,'username':username})


def login(request):
    print ("test")
    return render(request,'login.html')



def login_action(request):
    print("123")
    if request.method == 'POST':
        p_username = request.POST.get('user', '')
        p_password = request.POST.get('pwd', '')
        user = auth.authenticate(username=p_username, password=p_password)
        print(user)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = p_username
            response = HttpResponseRedirect('/blog/')
            #request.session['username'] = p_username
            return response
        else:
            # return HttpResponse("login failed")
            return render_to_response('login.html', {'error': "username or password incorrect"})
    else:
        return HttpResponse("not post!")

@login_required()
def logout(request):

    response = HttpResponseRedirect('/login/')
    del request.session['username']
    return  response


