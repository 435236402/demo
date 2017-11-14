from django.shortcuts import render,redirect

def index(request):
    return render(request,'booktest/index.html')

##装饰器判断用户是否登录
def login_required(view_func):
    def wrapper(request,*args,**kwargs):
        if request.session.has_key('islogin'):
            return view_func(request,*args,**kwargs)
        return redirect('/login')
    return wrapper




@login_required
def user(request):
    #判断用户是否登录
    # if not request.session.has_key('islogin'):
    #     return redirect('/login')
    return render(request,'booktest/user.html')


def login(request):
    #判断cookie中是否存在username  request.COOKIES
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request,'booktest/login.html',{'username':username})

def login_check(request):
    username = request.POST.get('username')
    userpassword = request.POST.get('userpassword')
    remember = request.POST.get('remember')

    if username == 'admin' and userpassword == '123':
        response = redirect('/index')
        #判断remember是否被勾选
        if remember == 'on':
            response.set_cookie('username',username,max_age=7*24*3600)
        else:
            response.delete_cookie('username')

        #只要session有islogin，就认为用户登录
        request.session['islogin'] = True
        request.session['username'] = username

        return response

    else:
        return redirect('/login')