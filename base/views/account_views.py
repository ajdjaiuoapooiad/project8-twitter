from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from base.models import Item,Profile
from django.contrib.auth import authenticate,login,logout  ##



def signupfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'pages/signup_login.html',{'error':'このユーザーはすでに使用されています'})
        except:
            user=User.objects.create_user(username2,'',password2)
            return redirect('/login/')
    return render(request,'pages/signup_login.html',{'some':100})

def loginfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        user=authenticate(username= username2,password=password2)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/signup/',{'error':'登録されていません'})
            
        
    return render(request,'pages/signup_login.html',{'some':100})


def logoutfunc(request):
    logout(request)
    return redirect('/login/')



##user_list------------------------

class UserView(generic.ListView):
    model=Item
    template_name='pages/user_list.html'
    
    def get_queryset(self):  ###追加
        current_user = self.request.user.username # ログイン中のユーザ名を取得（CustomUserモデルのusernameレコードの値を取得）
        user_data = User.objects.get(username=current_user) # QuerySet(条件が一致するレコードを全て取得)
        if user_data:
            queryset = Item.objects.filter(username=user_data).all() # QuerySet（一致するレコード全て取得）
          
        return queryset
    
    
    
class UserGoodView(generic.ListView):
    model=Item
    template_name='pages/user_good.html'
    
    def get_queryset(self):  ###追加
        current_user = self.request.user.username # ログイン中のユーザ名を取得（CustomUserモデルのusernameレコードの値を取得）
        user_data = User.objects.get(username=current_user) # QuerySet(条件が一致するレコードを全て取得)
        if user_data:
            queryset = Item.objects.filter(username=user_data).all() # QuerySet（一致するレコード全て取得）
          
        return queryset
    
class UserLikeView(generic.ListView):
    model=Item
    template_name='pages/user_like.html'
    
    def get_queryset(self):  ###追加
        current_user = self.request.user.username # ログイン中のユーザ名を取得（CustomUserモデルのusernameレコードの値を取得）
        user_data = User.objects.get(username=current_user) # QuerySet(条件が一致するレコードを全て取得)
        if user_data:
            queryset = Item.objects.filter(username=user_data).all() # QuerySet（一致するレコード全て取得）
          
        return queryset
    

##profile----------------------------

class ProfileUpdateView(generic.UpdateView):
    model=Profile
    template_name='pages/profile.html'
    fields={'name','image','bg_image'}
    success_url='/profile/'

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk']=self.request.user.pk
        return super().get_object()   
    
    
class AccountView(generic.UpdateView):
    model=User
    template_name='pages/account.html'
    fields={'username','email'}
    success_url='/account/'

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk']=self.request.user.pk
        return super().get_object()   
    
    
    
    