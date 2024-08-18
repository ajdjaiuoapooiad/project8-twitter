"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views
from django.conf import settings  # 増えた
from django.conf.urls.static import static  # 増えた

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    #User
    path('user/like/<int:pk>/',views.UserLikeView.as_view()), 
    path('user/good/<int:pk>/',views.UserGoodView.as_view()), 
    path('user/<int:pk>/',views.UserView.as_view()),  #userモデルのpkが入っている
    path('profile/',views.ProfileUpdateView.as_view()),
    path('account/',views.AccountView.as_view()),
    
    #Account
    path('logout/',views.logoutfunc),
    path('login/',views.loginfunc),
    path('signup/',views.signupfunc),
    
    #Item
    path('item/good/<str:pk>/',views.goodfunc),  ###
    
    path('item/delete/<str:pk>/',views.ItemDeleteView.as_view()),
    path('item/update/<str:pk>/',views.ItemUpdateView.as_view()),
    path('item/create/',views.ItemCreateView.as_view()),
    path('item/<str:pk>/',views.detailfunc),
    path('',views.ItemView.as_view()),
    
    
    
    #Category Tag
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
