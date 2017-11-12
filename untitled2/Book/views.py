from django.shortcuts import render
from django.http import HttpResponse

# def session_set(requset):
#     request.session['name'] = 'ithei
def set_session(request):
    '''设置session'''
    request.session['username']='smart'
    request.session['age']=18

    # 设置sessionid的过期时间
    # request.session.set_expiry(5)

    return HttpResponse('设置session')


def session_get(request):
    name = request.session['name']
    return HttpResponse(name)