from django.views import generic
from base.models import Item
from base.forms import ItemCreateForm
from  django.shortcuts import  render,redirect


class ItemView(generic.ListView):
    model=Item
    template_name='pages/item_list.html'
    
def detailfunc(request,pk):            ##変更
    ##追加  
    object=Item.objects.get(pk=pk)
    object.read_count += 1 #閲覧数をインクリメント
    object.save()
    return render(request,'pages/item_detail.html',{'object':object})
    
    
class ItemCreateView(generic.CreateView):
    model=Item
    template_name='pages/item_form.html'
    form_class=ItemCreateForm
    success_url='/'
    
class ItemUpdateView(generic.UpdateView):
    model=Item
    template_name='pages/item_update.html'
    form_class=ItemCreateForm
    success_url='/'
    
class ItemDeleteView(generic.DeleteView):
    model=Item
    template_name='pages/item_confim_delete.html'
    success_url='/'
    
    
##追加
def goodfunc(request,pk):
    item=Item.objects.get(pk=pk)
    item2=request.user.get_username()
    if item2 in item.usertext:
        return redirect('/')
    else:
        item.good_count += 1
        item.usertext = item.usertext + ' ' + item2   #空欄とusernameを追加する処理
        item.save()
        return redirect('/')
    