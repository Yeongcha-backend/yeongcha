from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Tip, Share
from django.utils import timezone
from .forms import QuestionModelForm, QuestionCommentForm, TipModelForm,  ShareModelForm, ShareCommentForm
# Create your views here.

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