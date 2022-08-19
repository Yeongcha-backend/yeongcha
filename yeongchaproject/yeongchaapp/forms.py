from django import forms
from .models import Question,QuestionComment,Tip,Share,ShareComment, Start

class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        #fields = '__all__'
        fields = ['title','body']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'input'
                }
            ),
            'body': forms.TextInput(
                attrs={
                    'class': 'input2',
                    'placeholder':'이곳에 글을 작성해주세요. 최소 10글자 이상 입력해주세요.'
                }
            )
        }

class QuestionCommentForm(forms.ModelForm):
    class Meta:
        model = QuestionComment
        fields =['comment']
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder':'댓글을 입력해주세요'
                }
            )
        }

class TipModelForm(forms.ModelForm):
    class Meta:
        model = Tip
        #fields = '__all__'
        fields = ['title','body']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'input'
                }
            ),
            'body': forms.TextInput(
                attrs={
                    'class': 'input2',
                    'placeholder':'이곳에 글을 작성해주세요. 최소 10글자 이상 입력해주세요.'
                }
            )
        }

class ShareModelForm(forms.ModelForm):
    class Meta:
        model = Share
        #exclude = ('finish',)
        #fields = '__all__'
        fields = ['title','body', 'count', 'photo']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'input'
                }
            ),
            'count': forms.TextInput(
                attrs={
                    'class': 'input3',
                    'placeholder':'예) 총 3개, 각 2개'
                }
            ),
            # 'photo': forms.TextInput(
            #     attrs={
            #         'class': 'file-upload'
            #     }
            # ),
            #   'rigon': forms.TextInput(
            #     attrs={
            #         'class': 'input3'
            #     }
            # ),
            'body':  forms.TextInput(
                attrs={
                    'class': 'input2',
                    'placeholder':'물품 설명이나 요청사항이 필요하다면 적어주세요'
                }
            )
        }

class ShareCommentForm(forms.ModelForm):
    class Meta:
        model = ShareComment
        fields =['comment']
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder':'댓글을 입력해주세요'
                }
            )
        }

class Start(forms.ModelForm):
    class Meta:
        model = Start
        fields=['first', 'second']