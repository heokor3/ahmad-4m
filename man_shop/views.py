from django.shortcuts import render, get_object_or_404
from . import models

def clothing_list(request):
    items = models.Clothingitem.objects.all()
    return render(request, 'man_shop/clothing_list.html', {'items': items})

def clothing_details(request, item_id):
    item = get_object_or_404(models.Clothingitem, pk=item_id)
    return render(request, 'man_shop/clothing_details.html', {'item': item})