from django.conf.urls import url
from Book import views

urlpatterns =[
    url(r'^set_session/$',views.set_session),
]