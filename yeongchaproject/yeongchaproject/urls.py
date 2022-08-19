from django.contrib import admin
from django.urls import path
from yeongchaapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('movingday/', views.movingday, name='movingday'),
    path('divide/',views.divide, name='divide'),
    path('movquote_strt/', views.movingquote_start, name='movingquote_start'),
    path('movquote_des/', views.movingquote_des, name='movingquote_des'),
    path('living/', views.living, name="living"),
    path('lib/',views.lib, name="lib"),
    path('digital/',views.digital, name="digital"),
    path('div/', views.divide, name="share"),
    path('det/', views.detail, name='detail'),
    path('kit/', views.kit, name='kit'),
    path('etc/', views.etc, name='etc'),
    path('mypg_mov/', views.mypg_mov, name="mypg_mov"),
    path('mypg_post/',views.mypg_post, name='mypg_post'),
    path('check_day/', views.check_day, name='check_day'),
    path('check_dday/', views.check_Dday, name='check_dday'),
    path('check_week/', views.check_week, name='check_week'),


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
    #이사견적 데이터 관련
    path('currentdata/', views.movingdata, name="movingdata"),
    
] #media 파일 접급할 수 있는 url 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
