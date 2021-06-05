from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-updated'] # 글 수정 시간의 내림차순으로 정렬

    def __str__(self): # 작성자의 이름과 글 작성일 반환
            return self.author.username+" "+self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):  # 객체의 상세 페이지 주소 반환
        return reverse('photo:photo_detail', args=[str(self.id)])