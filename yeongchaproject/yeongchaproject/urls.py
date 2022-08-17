"""yeongchaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from yeongchaapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'), #로그인 전 홈화면 

    path('login/',views.login,name='login'),
    path('main_home/',views.login_after,name='login_after'), #로그인 후 홈화면  
    path('signup/',views.signup,name='signup'),
    path('worker/', views.worker,name='worker'),
    path('worker_review/', views.worker_review,name='worker_review'),
    path('mypagereview',views.mypagereview,name='mypagereview'),
    #초보 이사러 관련 url 
    path('question/', views.question, name='question'),
    path('questioncreate/', views.questioncreate, name='questioncreate'),
    path('questiondetail/<int:question_id>', views.questiondetail, name='questiondetail'),
    path('questioncreate_comment/<int:question_id>', views.questioncreate_comment, name='questioncreate_comment'),
    #고수들의 꿀팁 관련 url 
    path('tip/', views.tip, name='tip'),
    path('tipcreate/', views.tipcreate, name='tipcreate'),
    path('tipdetail/<int:tip_id>', views.tipdetail, name='tipdetail'),
    #초보 이사러 관련 url 
    path('share/', views.share, name='share'),
    path('sharecreate/', views.sharecreate, name='sharecreate'),
    path('sharedetail/<int:share_id>', views.sharedetail, name='sharedetail'),
    path('sharecreate_comment/<int:share_id>', views.sharecreate_comment, name='sharecreate_comment'),

]
 #media 파일 접급할 수 있는 url 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
