from django.views import generic
from base.models import Item
from base.forms import ItemCreateForm


class ItemView(generic.ListView):
    model=Item
    template_name='pages/item_list.html'
    
class ItemDetailView(generic.DetailView):
    model=Item
    template_name='pages/item_detail.html'
    
class ItemCreateView(generic.CreateView):
    model=Item
    template_name='pages/item_form.html'
    form_class=ItemCreateForm
    success_url='/'
    
    