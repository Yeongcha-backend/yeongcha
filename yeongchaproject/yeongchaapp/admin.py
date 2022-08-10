from django.contrib import admin
from .models import Question, QuestionComment, Tip, Share, ShareComment
# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionComment)
admin.site.register(Tip)
admin.site.register(Share)
admin.site.register(ShareComment)