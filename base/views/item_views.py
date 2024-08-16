from django.views import generic
from base.models import Item


class ItemView(generic.ListView):
    model=Item
    template_name='pages/item_list.html'