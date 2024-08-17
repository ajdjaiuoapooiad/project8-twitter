from django.db import models
from django.utils.crypto import get_random_string
import os
from django.contrib.auth.models import User


##関数　　

def create_id():# urlから特定されないため   ランダムの文字列を入れる
    return get_random_string(22)
    
def upload_image_to(instance,filename):
    item_id=str(instance.id)
    return os.path.join('static/image','items',item_id,filename)


##models
    
class Category(models.Model):
    slug=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    slug=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


class Item(models.Model):
    id=models.CharField(primary_key=True,max_length=50,default=create_id,editable=False)
    text=models.TextField(max_length=1000)
    image=models.ImageField(upload_to=upload_image_to,default='',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    ##いいね　閲覧数
   
    read_count=models.PositiveIntegerField('閲覧数',default=0)
    good_count=models.PositiveIntegerField('いいね',default=0)
    usertext=models.CharField('user_itemの紐付け用',max_length=50,default='a')
    
 
    ##usernameとリンクさせる
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
  
    
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    tags=models.ManyToManyField(Tag,blank=True)
    
    def __str__(self):
        return self.text