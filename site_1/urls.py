"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lotto import views
urlpatterns = [
    #path('',views.index),
    path('admin/', admin.site.urls),
    #path('',views.index),#메인 도메인 주소(http://127.0.0.1:8000/)는 이미 적혀있는 상태임
    path('hello/',views.hello,name='hello_main'),
    path('lotto/',views.index,name='index'),
    path('lotto/new', views.post, name = "new_lotto"),
    path('lotto/<int:lottokey>/detail/', views.detail, name='detail'),
]#<데이터타입:views.py의 request 함수만 있었는데 그 뒤에 추가 파라미터 적을 수 있음
