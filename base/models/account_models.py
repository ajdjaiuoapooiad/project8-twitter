from django.db import models
from django.utils.crypto import get_random_string
import os
from django.contrib.auth.models import User
from base.models import create_id
from django.dispatch import receiver
from django.db.models.signals import post_save


##kokokara 関数





class Profile(models.Model):
    #Userとの紐付け
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)  ###
    name=models.CharField(max_length=50)
    image=models.ImageField('アイコン画像',upload_to='static/image/',default='static/sample_image/kkrn_icon_user_1.png',blank=True)
    bg_image=models.ImageField('背景画像',upload_to='static/image/',default='static/sample_image/pexels-eberhardgross-443446 (1).jpg',blank=True)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# OneToOneFieldを同時に作成
@receiver(post_save, sender=User)
def create_onetoone(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])