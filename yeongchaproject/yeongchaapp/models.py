from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    #photo = models.ImageField(blank=True, null=True, upload_to="question_photo")
    date =  models.DateTimeField(auto_now_add=True)
    counting = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class QuestionComment(models.Model):
    comment = models.TextField('')
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment

class Tip(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date =  models.DateTimeField(auto_now_add=True)
    counting = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Share(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    region = models.CharField(max_length=200)
    count = models.CharField(max_length=100)
    photo = models.ImageField( upload_to="share_photo")
    date =  models.DateTimeField(auto_now_add=True)
    finish = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class ShareComment(models.Model):
    comment = models.TextField('')
    data = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Share, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Start(models.Model):
    first = models.CharField(max_length=200)
    second = models.CharField(max_length=200)

    def __str__(self):
        return self.first