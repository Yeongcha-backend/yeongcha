from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Start, Tip, Share
from django.utils import timezone
from .forms import QuestionModelForm, QuestionCommentForm, TipModelForm,  ShareModelForm, ShareCommentForm
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request,'login_pre.html')

def login(request):
        # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')
        

def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
    # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return render(request, 'login_success.html')
    return render(request,'signup.html')

def login_after(request):
    return render(request,'login_after.html')

def worker(request):
    return render(request,'worker.html')

def worker_review(request):
    return render(request,'worker_review.html')

def mypagereview(request):
    return render(request,'mypage_review.html')
    
# 초보 이사러의 궁금증
def question(request):
    #posts = Blog.objects.all()
    posts = Question.objects.filter().order_by('-date')
    return render(request,'question.html',{'posts':posts})

def questioncreate(request):
    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question')
    else:
        form = QuestionModelForm()
    #tㅔ번쨰 인자는 딕셔너리 형태
    return render(request, 'question_create.html', {'form':form})
    
def questiondetail(request,question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    question_detail.counting += 1
    question_detail.save()
    commnet_form = QuestionCommentForm()
    return render(request, 'question_detail.html',{'question_detail':question_detail,'commnet_form':commnet_form})

def questioncreate_comment(request, question_id):
        filled_form = QuestionCommentForm(request.POST)

        if filled_form.is_valid():
            finished_form = filled_form.save(commit=False)
            finished_form.post = get_object_or_404(Question, pk=question_id)
            finished_form.save()
        return redirect('questiondetail',question_id)

# 고수의 꿀팁
def tip(request):
    #posts = Blog.objects.all()
    posts = Tip.objects.filter().order_by('-date')
    return render(request,'tip.html',{'posts':posts})

def tipcreate(request):
    if request.method == 'POST':
        form = TipModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tip')
    else:
        form = TipModelForm()
    #tㅔ번쨰 인자는 딕셔너리 형태
    return render(request, 'tip_create.html', {'form':form})
    
def tipdetail(request,tip_id):
    tip_detail = get_object_or_404(Tip, pk=tip_id)
    tip_detail.counting += 1
    tip_detail.save()
    return render(request, 'tip_detail.html',{'tip_detail':tip_detail})

# 나눔 장터
def share(request):
    #posts = Blog.objects.all()
    posts = Share.objects.filter().order_by('-date')
    return render(request,'share.html',{'posts':posts})

def sharecreate(request):
    if request.method == 'POST' or request.method == "FILES":
        form = ShareModelForm(request.POST, request.FILES)
        #form.region = request.POST.get("sido1")
        if form.is_valid():
            form.region = request.POST.get("sido1")
            form.save()
            return redirect('share')
    else:
        form = ShareModelForm()
    #tㅔ번쨰 인자는 딕셔너리 형태
    return render(request, 'share_create.html', {'form':form})
    
def sharedetail(request,share_id):
    share_detail = get_object_or_404(Share, pk=share_id)

    commnet_form = ShareCommentForm()
    return render(request, 'share_detail.html',{'share_detail':share_detail,'commnet_form':commnet_form})

def sharecreate_comment(request, share_id):
        filled_form = ShareCommentForm(request.POST)

        if filled_form.is_valid():
            finished_form = filled_form.save(commit=False)
            finished_form.post = get_object_or_404(Share, pk=share_id)
            finished_form.save()
        return redirect('sharedetail',share_id)
#상단바 url
def home(request):
    return render(request, 'login_pre.html')

def movingday(request):
    return render(request, 'movingDay.html')

def divide(request):
    return render(request, 'divide.html')

def movingquote_start(request):
    return render(request, 'movingQuote_start.html')

#견적 파트 url 
def movingquote_des(request):
    return render(request, 'movingQuote_des.html')

def living(request):
    return render(request, 'bed_living.html')

def lib(request):
    return render(request, 'lib.html')

def digital(request):
    return render(request, 'digital.html')

def kit(request):
    return render(request, 'kitchen.html')

def detail(request):
    return render(request, 'detail.html')

def mypg_mov(request):
    return render(request, 'mypage_moving.html')

def mypg_post(request):
    return render(request, 'mypage_post.html')

def check_day(request):
    return render(request, 'checklist_day.html')

def check_Dday(request):
    return render(request, 'checklist_Dday.html')

def check_week(request):
    return render(request, 'checklist_week.html')
    
def etc(request):
    return render(request, 'etc.html')



#이사견적 데이터
def movingdata(request):
    if request.method == 'POST':
        form=Start(request.POST)
        if form.is_vaild():
            post=form.save(commit=False)
            post.save()
            return render(request, 'final_review_fin.html')
        else:
            return render(request, 'final_review_fin.html')
    return render()
    